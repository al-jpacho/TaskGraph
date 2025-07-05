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


def load_tasks(file_path: str) -> list[dict]:
    """
    Load the most recent TaskGraph JSON file from a folder.

    Args:
        file_path (str): Directory path to JSON file.

    Raises:
        FileNotFoundError: No TaskGraph file found.

    Returns:
        list[dict]: List of task objects.
    """
    files = sorted(
        f for f in os.listdir(file_path)
        if f.startswith("taskgraph-") and f.endswith(".json")
    )

    if not files:
        raise FileNotFoundError("No TaskGraph JSON files found.")

    file_to_open = os.path.join(file_path, files[-1])

    with open(file_to_open, "r", encoding="utf-8") as f:
        tasks = json.load(f)

    return tasks

