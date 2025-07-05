from typing import List, Tuple, Optional

def parse_dependencies(line: str) -> List[Tuple[str, Optional[str]]]:
    """
    Parse a task dependency chain from a single line of input.
    Splits by '->' to extract parent, child pairs.
    Single task return (parent, None) tuples.

    Args:
        line (str): Represents chain of tasks, using '->' to 
            separate tasks.

    Returns:
        List[Tuple[str, Optional[str]]]: A list of (parent, child) pairs.
        If a task has no dependency, its child will be None.
    """
    tokens = [t.strip() for t in line.split("->")]

    if len(tokens) < 2: 
        return [(tokens[0], None)]

    pairs = []
    for i in range(len(tokens) - 1):
        parent = tokens[i]
        child = tokens[i + 1]
        pairs.append((parent, child))

    return pairs


def extract_status(task_str: str) -> Tuple[str, Optional[str]]:
    """
    Extracts task name and status. 

    Supported status tags: 
        [todo], [inProgress], [done]
    
    Defaults to None if there is no status.

    Args:
        task_str (str): Task name and possibly status tag.

    Returns:
        Tuple[str, str]: (Task name, Status)
    """
    task_str = task_str.strip()

    if task_str.endswith("[todo]"):
        return task_str[:-6].strip(), "todo"
    elif task_str.endswith("[inProgress]"):
        return task_str[:-10].strip(), "inProgress"
    elif task_str.endswith("[done]"):
        return task_str[:-6].strip(), "done"
    else: 
        return task_str, None


def parse_input_data(text: str) -> list[dict]:
    """
    Parses multiline text into a list of task dependencies.

    Each item in the list represents a task and its dependencies
    Args:
        text (str): Multiline string of task definitions.

    Returns:
        list[dict]: List of task dictionaries with 'task' and
        what it 'depends_on'.
    """

    tasks = {}

    for line in text.strip().splitlines():
        links = parse_dependencies(line)

        for parent, child in links: 
            if parent not in tasks:
                tasks[parent] = {"task": parent, "depends_on": []}

            if child:
                if child not in tasks:
                    tasks[child] = {"task": child, "depends_on": []}
                    tasks[child]["depends_on"].append(parent)


    return list(tasks.values())