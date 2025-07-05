# TaskGraph

TaskGraph is a lightweight productivity tool for visualising your tasks as a dependency graph — combining elements of a mind map and a directed acyclic graph (DAG). It’s designed to help you think clearly, plan intentionally, and act with focus.

---

## What It Does (v1.0.2)

- Parse simple task inputs like:
  ```
  [Category A] Task X [todo] -> Task Y [inProgress]
  Task Z [done]
  ```
- Build a directed task graph with dependencies
- Assign `status` to each task: `todo`, `inProgress`, or `done`
- Visualise the graph in a Streamlit interface
- Export structured task data as JSON

---

## Features

- DAG construction using `networkx`
- Streamlit UI for task input and visualisation
- Inline parsing of categories and statuses
- JSON output for storing and reviewing structured task data

---

## Tech Stack

| Component        | Tool / Library           |
|------------------|--------------------------|
| Language         | Python                   |
| UI Framework     | Streamlit                |
| Graph Logic      | networkx                 |
| Visual Rendering | matplotlib               |
| Input Parsing    | Custom regex             |
| Data Format      | JSON (YAML coming soon)  |

---

## Project Structure

```
taskgraph/
├── core.py                  # Parses tasks and dependencies
├── ui/
│   ├── visualise.py         # Renders the graph using networkx
│   └── streamlit_app.py     # Streamlit front-end
tests/
└── test_core.py             # Unit tests for parsing logic
```

---

## Usage

### Run Locally

```bash
git clone https://github.com/your-username/taskgraph.git
cd taskgraph
PYTHONPATH=. streamlit run taskgraph/ui/streamlit_app.py
```

### Sample Input Format

```
[Category A] Task X [todo] -> Task Y [inProgress]
[Category B] Task Z [done]
Task A [todo] -> Task B [inProgress] -> Task C
```

- `[]` indicates optional metadata (e.g., `[Category A]`, `[todo]`)
- `->` indicates task dependency (Task A must be done before Task B)

---

## License

Apache 2.0

---

## Author

Built and maintained by [@al-jpacho](https://github.com/al-jpacho).
