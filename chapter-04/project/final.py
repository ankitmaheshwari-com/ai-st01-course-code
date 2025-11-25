import streamlit as st
import uuid
import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="ProTasker", layout="centered")

# --- 1. BACKEND / LOGIC FUNCTIONS ---
# We keep these at the top to keep the code organized

def init_state():
    """Initialize session state if it doesn't exist."""
    if "tasks" not in st.session_state:
        # Structure: {'id': str, 'title': str, 'done': bool, 'priority': str, 'created_at': str}
        st.session_state.tasks = []

def add_task():
    """Callback to add a new task."""
    task_title = st.session_state.new_task_input
    priority = st.session_state.new_task_priority
    
    if task_title.strip():
        new_task = {
            "id": str(uuid.uuid4()),  # Generates a unique ID (e.g., 'a1-b2-c3')
            "title": task_title.strip(),
            "done": False,
            "priority": priority,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        st.session_state.tasks.append(new_task)
        # Clear the input field after adding
        st.session_state.new_task_input = ""

def delete_task(task_id):
    """Callback to delete a task by its unique ID."""
    st.session_state.tasks = [t for t in st.session_state.tasks if t["id"] != task_id]

def toggle_status(task_id):
    """Callback to toggle the done status."""
    for task in st.session_state.tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            break

def get_metrics():
    """Helper to get task counts."""
    total = len(st.session_state.tasks)
    completed = len([t for t in st.session_state.tasks if t["done"]])
    return total, completed

# --- 2. INITIALIZATION ---
init_state()

# --- 3. UI HEADER & METRICS ---
st.title("ProTasker")
st.caption("Manage your sprint effectively with priority tracking.")

# Dashboard Progress Bar
total_tasks, completed_tasks = get_metrics()
if total_tasks > 0:
    progress = completed_tasks / total_tasks
    st.progress(progress)
    st.caption(f"Progress: {int(progress * 100)}% completed")
else:
    st.info("Start by adding your first task below!")

st.divider()

# --- 4. INPUT SECTION ---
# Using a container to group the input controls visually
with st.container(border=True):
    c1, c2, c3 = st.columns([3, 1, 1])
    
    with c1:
        st.text_input(
            "Task Title", 
            placeholder="e.g., Go to Gym...", 
            key="new_task_input", 
            label_visibility="collapsed"
        )
    
    with c2:
        st.selectbox(
            "Priority", 
            ["🔥 High", "⚡ Medium", "☕ Low"], 
            key="new_task_priority", 
            label_visibility="collapsed"
        )
    
    with c3:
        # on_click calls the function BEFORE the app reruns
        st.button("Add Task", type="primary", on_click=add_task, use_container_width=True)

# --- 5. TASK LIST RENDERER ---
st.subheader("Your Board")

# Using Tabs to separate Active vs Completed tasks
tab_active, tab_completed = st.tabs(["📌 Active Tasks", "🎉 Completed"])

def render_task_row(task, is_completed_tab=False):
    """Helper to render a single task row."""
    
    # define colors based on priority
    priority_colors = {"🔥 High": "red", "⚡ Medium": "orange", "☕ Low": "green"}
    color = priority_colors.get(task['priority'], "grey")

    with st.container(border=True):
        col1, col2, col3, col4 = st.columns([0.05, 0.7, 0.15, 0.1])
        
        with col1:
            st.checkbox(
                "", 
                value=task["done"], 
                key=f"check_{task['id']}", 
                on_change=toggle_status, 
                args=(task['id'],)
            )
        
        with col2:
            if is_completed_tab:
                st.markdown(f"~~{task['title']}~~")
            else:
                st.markdown(f"**{task['title']}**")
            st.caption(f"Created: {task['created_at']}")

        with col3:
            st.markdown(f":{color}[{task['priority']}]")

        with col4:
            st.button(
                "🗑️", 
                key=f"del_{task['id']}", 
                on_click=delete_task, 
                args=(task['id'],)
            )

# --- 6. DISPLAY LOGIC ---
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