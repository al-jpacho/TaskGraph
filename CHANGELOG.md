# Changelog

All notable changes to this project will be documented in this file.

---

## [v1.0.3] - 2025-07-10

### New Features
- Added support for task `status` markers (`[todo]`, `[inProgress]`, `[done]`)
- Visualised node `roles` using shape:
  - Start nodes: squares
  - End nodes: diamonds
  - Middle nodes: circles
- Multiselect filter in Streamlit UI to filter tasks by status
- Export task graph as timestamped JSON
- Load the most recent saved task graph on demand

### Unit Testing
- `test_core.py`:
  - `extract_status`, `parse_dependencies`, `parse_input_data`, `assign_node_roles`
- `test_io.py`:
  - `test_save_tasks_create_file`: Ensures a timestamped file is created correctly
  - `test_save_tasks_content`: Verifies that the saved file matches the task list
  - `test_load_tasks_success`: Confirms that a saved file can be loaded correctly
  - `test_load_tasks_no_files`: Asserts that a `FileNotFoundError` is raised when no files exist

### Visual Styling
- Refactored node styling to separate roles by shape and status by colour
- Dual legend support in matplotlib: one for status, one for roles
- Improved Streamlit layout for better UX

### Infrastructure
- Introduced `pytest.ini` to set PYTHONPATH
- Initialised clean `tests/` directory scaffold

---

## [v1.0.2] - 2025-07-08

### Features
- Added save/load functionality for graphs using JSON
- File saving includes timestamp to avoid overwriting
- Automatically loads most recent saved graph
- Streamlit UI updated with buttons for save/load
- Added data persistence directory (`taskgraph/data/`)

### UX
- Streamlit uses `st.session_state` to preserve user data
- Status messages and warnings guide user interactions

---

## [v1.0.1] - 2025-07-06

### Improvements
- Graph rendering size scaled for smaller screens
- Added Markdown section separators in Streamlit
- Buttons grouped horizontally for better layout
- Streamlit state more clearly managed between interactions

---

## [v1.0.0] - 2025-07-04

### Initial MVP
- Users can input plain text task dependencies using `->` syntax
- Parsed task relationships visualised using NetworkX + Matplotlib
- Streamlit app renders task graph with colour by status
- Task data structure includes:
  - `task` (str)
  - `depends_on` (List[str])
- Included basic parser for dependency chains
