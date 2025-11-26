import streamlit as st
import data_manager as dm
import state_manager as sm
import ui_components as ui

# 1. Load Data
raw_data = dm.load_initial_data()

# 2. Initialize Session State
sm.init_session_state(len(raw_data))

# 3. Main UI Layout
ui.render_header(len(st.session_state.labels), len(raw_data))

# --- PAGINATION LOGIC ---
# Get the current item based on the index stored in session state
current_index = st.session_state.current_index
current_item = raw_data[current_index]

# Check if this item already has a label in session state
existing_label = st.session_state.labels.get(current_item['id'])

# --- RENDER CARD ---
ui.render_item_card(current_item, existing_label)

# --- CONTROLS SECTION ---
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    # "Previous" Button - Triggers callback
    st.button("⬅ Previous", on_click=sm.prev_item, disabled=(current_index == 0))

with col2:
    # Labeling Buttons
    # Note: We use lambda or args to pass data to the callback
    c1, c2, c3 = st.columns(3)
    c1.button("Positive", type="primary", use_container_width=True, 
              on_click=sm.submit_label, args=(current_item['id'], "Positive"))
    c2.button("Neutral", use_container_width=True, 
              on_click=sm.submit_label, args=(current_item['id'], "Neutral"))
    c3.button("Negative", type="primary", use_container_width=True, 
              on_click=sm.submit_label, args=(current_item['id'], "Negative"))

with col3:
    # "Next" Button - Triggers callback
    st.button("Next ➡", on_click=sm.next_item, disabled=(current_index == len(raw_data) - 1))

# --- SIDEBAR & EXPORT ---
ui.render_sidebar_metrics(st.session_state.labels)

st.sidebar.divider()
if st.sidebar.button("Export Results to CSV"):
    df = dm.convert_state_to_dataframe(st.session_state.labels)
    st.sidebar.dataframe(df) # Preview

