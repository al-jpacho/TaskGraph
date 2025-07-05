import os

import streamlit as st

from taskgraph.core import parse_input_data
from taskgraph.io import load_tasks, save_tasks
from taskgraph.ui.visualise import generate_task_graph

DATA_PATH = "taskgraph/data/"
os.makedirs(DATA_PATH, exist_ok=True)

st.set_page_config(page_title="TaskGraph", layout="wide")
st.title("TaskGraph")

# Session setup
if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

# --- Input section ---
user_input = st.text_area(
    "Enter tasks (use -> for dependencies)",
    height=200,
    placeholder="Example:\nTask A -> Task B -> Task C\nTask D",
)

st.markdown("---")
st.subheader("Actions")

# --- Button section ---
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Generate Graph") and user_input.strip():
        st.session_state["tasks"] = parse_input_data(user_input)

with col2:
    if st.button("Save Graph"):
        if st.session_state["tasks"]:
            save_tasks(st.session_state["tasks"], DATA_PATH)
            st.success("Graph saved sucessfully.")
        else:
            st.warning("There is nothing to save — generate a graph first.")

with col3:
    if st.button("Load Graph"):
        try:
            st.session_state["tasks"] = load_tasks(DATA_PATH)
            st.success("Latest saved graph loaded.")
        except FileNotFoundError:
            st.warning("No saved graph files found.")

st.markdown("---")

# --- Output section ---
if st.session_state["tasks"]:
    st.subheader("Parsed Task Data")
    st.json(st.session_state["tasks"])

    status_filter = st.multiselect(
        "Show tasks with status:", 
        options=["todo", "inProgress", "done"],
        default=["todo", "inProgress", "done"]
    )

    st.subheader("Graph View")
    generate_task_graph(st.session_state["tasks"])
else:
    st.info("No graph loaded yet. Enter tasks above or laod a saved graph.")
