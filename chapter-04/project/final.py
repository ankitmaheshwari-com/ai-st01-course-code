import streamlit as st

st.set_page_config(page_title="To-Do List", page_icon="📝")

# -------------------------------------
# Initialize Session State
# -------------------------------------
if "tasks" not in st.session_state:
    st.session_state.tasks = []       # List of {"task": "...", "done": False}

if "new_task" not in st.session_state:
    st.session_state.new_task = ""

# -------------------------------------
# Add Task Handler
# -------------------------------------
def add_task():
    task_text = st.session_state.new_task.strip()
    if task_text:
        st.session_state.tasks.append({"task": task_text, "done": False})
        st.session_state.new_task = ""   # Clear input field

# -------------------------------------
# Toggle Task Done
# -------------------------------------
def toggle_done(index):
    st.session_state.tasks[index]["done"] = not st.session_state.tasks[index]["done"]

# -------------------------------------
# Delete Task
# -------------------------------------
def delete_task(index):
    st.session_state.tasks.pop(index)

# -------------------------------------
# UI Layout
# -------------------------------------
st.title("📝 To-Do List")
st.write("A simple to-do manager using **Streamlit Session State**.")

st.text_input("Add a new task:", key="new_task", on_change=add_task)

st.write("### Your Tasks")

if not st.session_state.tasks:
    st.info("No tasks yet. Add something above!")
else:
    # Display each task dynamically
    for i, task in enumerate(st.session_state.tasks):
        
        col1, col2, col3 = st.columns([0.07, 0.7, 0.2])

        with col1:
            st.checkbox(
                "",
                value=task["done"],
                key=f"done_{i}",
                on_change=toggle_done,
                args=(i,),
            )

        with col2:
            task_text = f"~~{task['task']}~~" if task["done"] else task["task"]
            st.write(task_text)

        with col3:
            st.button("❌ Delete", key=f"delete_{i}", on_click=delete_task, args=(i,))

# Optional footer
st.write("---")
st.caption("Built with ❤️ using Streamlit & Session State.")
