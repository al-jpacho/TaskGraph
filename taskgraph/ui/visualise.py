import networkx as nx 
import matplotlib.pyplot as plt
import streamlit as st

STATUS_COLOURS = {
    "todo": "lightgrey",
    "inProgress": "lightblue",
    "done": "limegreen",
    None: "grey"
}

def generate_task_graph(tasks: list[dict]):
    """
    Generates a visual task dependency graph from a list of task dictionaries.

    Args:
        tasks (list[dict]): Each dictionary must contain 'task' and 'depends_on'.
    """
    G = nx.DiGraph()

    node_colours = []

    for task in tasks:
        task_name = task["task"]
        status = task["status"]

        G.add_node(task_name)
        node_colours.append(STATUS_COLOURS[status])
    
    for task in tasks:
        for dep in task["depends_on"]:
            G.add_edge(dep, task["task"])

    pos = nx.spring_layout(G, k=0.5)

    fig, ax = plt.subplots(figsize=(8,3))
    nx.draw(G, pos, with_labels=True, arrows=True, node_size=400, node_color=node_colours, font_size=5, ax=ax)
    st.pyplot(fig) 