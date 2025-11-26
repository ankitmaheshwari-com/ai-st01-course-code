# ui.py

import streamlit as st
from logic import add_task, delete_task, toggle_status, get_metrics

# Helper data for styling
PRIORITY_COLORS = {"🔥 High": "red", "⚡ Medium": "orange", "☕ Low": "green"}

def render_header():
    """Renders the application title and dynamic progress bar."""
    st.title("ProTasker")
    st.caption("Manage your sprint effectively with priority tracking.")

    total_tasks, completed_tasks = get_metrics() 
    if total_tasks > 0:
        progress = completed_tasks / total_tasks
        st.progress(progress)
        st.caption(f"Progress: {int(progress * 100)}% completed")
    else:
        st.info("Start by adding your first task below!")
    st.divider()

def render_input():
    """Renders the task input form."""
    with st.container(border=True):
        c1, c2, c3 = st.columns([3, 1, 1])
        
        with c1:
            st.text_input("Task Title", placeholder="e.g., Go to Gym...", key="new_task_input", label_visibility="collapsed")
        with c2:
            st.selectbox("Priority", ["🔥 High", "⚡ Medium", "☕ Low"], key="new_task_priority", label_visibility="collapsed")
        with c3:
            st.button("Add Task", type="primary", on_click=add_task, use_container_width=True)

def render_task_row(task, is_completed_tab=False):
    """Renders a single task row layout."""
    color = PRIORITY_COLORS.get(task['priority'], "grey")

    with st.container(border=True):
        # Adjusted column widths slightly since the caption is gone
        col1, col2, col3, col4 = st.columns([0.05, 0.75, 0.15, 0.05])
        
        with col1:
            st.checkbox("", value=task["done"], key=f"check_{task['id']}", 
                        on_change=toggle_status, args=(task['id'],))
        with col2:
            title = f"~~{task['title']}~~" if is_completed_tab else f"**{task['title']}**"
            st.markdown(title)
            # Removed st.caption(f"Created: {task['created_at']}")
        with col3:
            st.markdown(f":{color}[{task['priority']}]")
        with col4:
            st.button("🗑️", key=f"del_{task['id']}", on_click=delete_task, args=(task['id'],))

def render_tasks():
    """Renders the task list, including tab filtering and bulk action."""
    st.subheader("Your Board")
    tab_active, tab_completed = st.tabs(["📌 Active Tasks", "🎉 Completed"])

    with tab_active:
        active_tasks = [t for t in st.session_state.tasks if not t["done"]]
        if not active_tasks:
            st.info("No active tasks! Enjoy your day. 😎")
        else:
            for task in active_tasks:
                render_task_row(task)

    with tab_completed:
        done_tasks = [t for t in st.session_state.tasks if t["done"]]
        if not done_tasks:
            st.write("No completed tasks yet.")
        else:
            if st.button("Clear All Completed"):
                st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
                st.rerun()
                
            for task in done_tasks:
                render_task_row(task, is_completed_tab=True)