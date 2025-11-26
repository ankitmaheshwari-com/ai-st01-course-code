import streamlit as st

def init_session_state(total_items):
    """
    Initializes the session state variables if they don't exist.
    """
    # 1. Pagination State: Tracks which item index we are currently viewing
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0
    
    # 2. Data State: Stores the labels user has assigned {id: label}
    if 'labels' not in st.session_state:
        st.session_state.labels = {}

    # 3. Meta State: Just to track total count for progress bars
    if 'total_items' not in st.session_state:
        st.session_state.total_items = total_items

# --- CALLBACKS ---
# These functions are called directly by widgets (buttons). 
# They handle logic BEFORE the app reruns.

def next_item():
    """Pagination Logic: Move forward"""
    if st.session_state.current_index < st.session_state.total_items - 1:
        st.session_state.current_index += 1

def prev_item():
    """Pagination Logic: Move backward"""
    if st.session_state.current_index > 0:
        st.session_state.current_index -= 1

def submit_label(item_id, label):
    """
    1. Saves the label to session state.
    2. Automatically triggers 'next_item' to improve workflow speed.
    """
    st.session_state.labels[item_id] = label
    
    # Auto-advance functionality (User Experience upgrade)
    if st.session_state.current_index < st.session_state.total_items - 1:
        st.session_state.current_index += 1