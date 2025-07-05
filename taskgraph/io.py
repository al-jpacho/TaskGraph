import json
import os
from datetime import datetime


def save_tasks(json_data: list[dict], file_path: str) -> None:
    """
    Save JSON task data as a timestamped JSON file in a specified folder.

    Args:
        json_data (list[dict]): List of task objects to save.
        file_path (str): Directory path to save JSON file.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    full_path = os.path.join(file_path, f"taskgraph-{timestamp}.json")

    with open(full_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2)


def load_tasks():
    """ """
    pass
