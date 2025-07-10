from typing import Dict, List

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

from taskgraph.core import assign_node_roles

STATUS_COLORS = {
    "todo": "lightgrey",
    "inProgress": "lightblue",
    "done": "limegreen",
    None: "grey",
}

ROLE_SHAPES = {"start": "s", "end": "d", "middle": "o"}


def generate_task_graph(tasks: List[Dict]):
    """
    Generates a visual task dependency graph from a List of task Dictionaries.

    Args:
        tasks (List[Dict]): Each Dictionary must contain 'task' and 'depends_on'.
    """
    G = nx.DiGraph()
    node_roles = assign_node_roles(tasks)
    task_names = {task["task"] for task in tasks}

    # --- Add nodes and edges ---
    for task in tasks:
        G.add_node(task["task"])

    for task in tasks:
        for dep in task["depends_on"]:
            if dep in task_names:
                G.add_edge(dep, task["task"])

    pos = nx.spring_layout(G, k=0.5)

    fig, ax = plt.subplots(figsize=(8, 3))

    # --- Draw nodes and edges based on roles --

    for role, shape in ROLE_SHAPES.items():
        role_nodes = [
            task["task"] for task in tasks if node_roles[task["task"]] == role
        ]
        role_colors = [
            STATUS_COLORS.get(task["status"], "grey")
            for task in tasks
            if node_roles[task["task"]] == role
        ]

        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist=role_nodes,
            node_color=role_colors,
            node_shape=shape,
            node_size=400,
            ax=ax,
        )

    nx.draw_networkx_edges(G, pos, ax=ax, arrows=True)
    nx.draw_networkx_labels(G, pos, font_size=5, ax=ax)

    # --- Legends ---
    color_legend = [
        Patch(color=color, label=status if status else "None")
        for status, color in STATUS_COLORS.items()
    ]

    shape_legend = [
        Line2D(
            [0],
            [0],
            marker=shape,
            color="w",
            label=role.title(),
            markerfacecolor="grey",
            markersize=8,
        )
        for role, shape in ROLE_SHAPES.items()
    ]

    ax.legend(
        handles=color_legend + shape_legend,
        loc="lower left",
        fontsize="x-small",
        frameon=False,
    )

    ax.set_title("Task Dependency Graph")

    return fig
