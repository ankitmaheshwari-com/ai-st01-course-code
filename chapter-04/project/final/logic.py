# logic.py

import streamlit as st
import uuid

def init_state():
    """Initializes session state if it doesn't exist."""
    if "tasks" not in st.session_state:
        # Simplified structure: {'id': str, 'title': str, 'done': bool, 'priority': str}
        st.session_state.tasks = []

def add_task():
    """Callback to create and append a new task to the state."""
    task_title = st.session_state.new_task_input
    priority = st.session_state.new_task_priority
    
    if task_title.strip():
        new_task = {
            "id": str(uuid.uuid4()),
            "title": task_title.strip(),
            "done": False,
            "priority": priority,
          
        }
        st.session_state.tasks.append(new_task)
        st.session_state.new_task_input = ""

def delete_task(task_id):
    """Filters the task list to remove the task with the given ID."""
    st.session_state.tasks = [t for t in st.session_state.tasks if t["id"] != task_id]

def toggle_status(task_id):
    """Toggles the 'done' status for a task found by its ID."""
    for task in st.session_state.tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            break

def get_metrics():
    """Calculates total and completed task counts for the header."""
    total = len(st.session_state.tasks)
    completed = len([t for t in st.session_state.tasks if t["done"]])
    return total, completed