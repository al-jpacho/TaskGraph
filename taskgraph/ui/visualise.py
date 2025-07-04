import networkx as nx 
import matplotlib.pyplot as plt

def generate_task_graph(tasks: list[dict]):
    """
    Generates a visual task dependency graph from a list of task dictionaries.

    Args:
        tasks (list[dict]): Each dictionary must contain 'task' and 'depends_on'.
    """
    G = nx.Graph()

    for task in tasks:
        G.add_node(task["task"])
    
    for task in tasks:
        for dep in task["depends_on"]:
            G.add_edge(dep, task["task"])

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, arrows=True, node_size=1500, node_color='green', font_size=10)
    plt.title("Task Dependency Graph")
    plt.show()