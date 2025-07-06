from taskgraph.core import extract_status

def test_extract_status_todo():
    assert extract_status("Task A [todo]") == ("Task A", "todo")


def test_extract_status_done():
    assert extract_status("Task B [done]") == ("Task B", "done")


def test_extract_status_in_progress():
    assert extract_status("Task C [inProgress]") == ("Task C", "inProgress")


def test_extract_status_no_tag():
    assert extract_status("Task D") == ("Task D", None)
