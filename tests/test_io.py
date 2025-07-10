import json
import os

import pytest

from taskgraph.io import load_tasks, save_tasks


@pytest.fixture
def sample_tasks():
    return [
        {"task": "Task A", "depends_on": [], "status": "todo"},
        {"task": "Task B", "depends_on": ["Task A"], "status": "done"},
        {"task": "Task C", "depends_on": ["Task A"], "status": "inProgress"},
    ]


def test_save_tasks_create_file(sample_tasks, tmp_path):
    save_tasks(sample_tasks, tmp_path)

    # Check if the file is created
    files = os.listdir(tmp_path)
    assert len(files) == 1
    assert files[0].startswith("taskgraph-") and files[0].endswith(".json")


def test_save_tasks_content(sample_tasks, tmp_path):
    save_tasks(sample_tasks, tmp_path)

    # Check the content of the created file
    files = os.listdir(tmp_path)
    file_path = tmp_path / files[0]

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert data == sample_tasks


def test_load_tasks_success(sample_tasks, tmp_path):
    # Save tasks first
    save_tasks(sample_tasks, tmp_path)

    # Load tasks and verify the content
    loaded_tasks = load_tasks(tmp_path)
    assert loaded_tasks == sample_tasks


def test_load_tasks_no_files(tmp_path):
    # Ensure the directory is empty
    assert not os.listdir(tmp_path)

    # Attempt to load tasks and expect a FileNotFoundError
    with pytest.raises(
        FileNotFoundError, match="No TaskGraph JSON files found."
    ):
        load_tasks(tmp_path)
