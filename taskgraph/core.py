from typing import List, Tuple, Optional, Dict


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


def parse_input_data(text: str) -> list[Dict[str, object]]:
    """
    Parses multiline task input into a structured list of task dictionaries.

    Each line may define a task or a dependency chain using '->'.
    Tasks can optionally include a status tag like [todo], [inProgress], or [done].

    Example:
        Task A [done] -> Task B [todo]
        Task C

    Args:
        text (str): Multiline string of task definitions.

    Returns:
        List[Dict[str, object]]: List of task dictionaries. Each has:
            - 'task' (str): Task name
            - 'depends_on' (List[str]): Parent task names
            - 'status' (str): Task status ("todo", "done", etc.)
    """

    tasks = {}

    for line in text.strip().splitlines():
        pairs = parse_dependencies(line)

        for parent_raw, child_raw in pairs:
            parent, parent_status = extract_status(parent_raw)

            if parent not in tasks:
                tasks[parent] = {
                    "task": parent,
                    "depends_on": [],
                    "status": parent_status,
                }

            if child_raw is not None:
                child, child_status = extract_status(child_raw)

                if child not in tasks:
                    tasks[child] = {
                        "task": child,
                        "depends_on": [],
                        "status": child_status,
                    }

                if parent not in tasks[child]["depends_on"]:
                    tasks[child]["depends_on"].append(parent)

    return list(tasks.values())
