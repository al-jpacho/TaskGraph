import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from typing import List, Dict
from taskgraph.core import assign_node_roles

STATUS_COLORS = {
    "todo": "lightgrey",
    "inProgress": "lightblue",
    "done": "limegreen",
    None: "grey",
}



def generate_task_graph(tasks: List[Dict]):
    """
    Generates a visual task dependency graph from a List of task Dictionaries.

    Args:
        tasks (List[Dict]): Each Dictionary must contain 'task' and 'depends_on'.
    """
    G = nx.DiGraph()

    node_colors = []

    node_roles = assign_node_roles(tasks)

    task_names = {task["task"] for task in tasks}

    for task in tasks:
        task_name = task["task"]
        status = task["status"]

        G.add_node(task_name)
        node_colors.append(STATUS_COLORS.get(status, "grey"))

    for task in tasks:
        for dep in task["depends_on"]:
            if dep in task_names and task["task"] in task_names:
                G.add_edge(dep, task["task"])

    pos = nx.spring_layout(G, k=0.5)

    fig, ax = plt.subplots(figsize=(8, 3))

    legend_elements = [
        Patch(color=color, label=status) for status, color in STATUS_COLORS.items()
    ]

    ax.legend(
        handles=legend_elements, loc="lower left", fontsize="x-small", frameon=False
    )

    nx.draw(
        G,
        pos,
        with_labels=True,
        arrows=True,
        node_size=400,
        node_color=node_colors,
        font_size=5,
        ax=ax,
    )
    return fig
