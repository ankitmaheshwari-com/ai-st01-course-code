# app.py

import streamlit as st
from logic import init_state
from ui import render_header, render_input, render_tasks

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="ProTasker", layout="centered")

# --- 2. INITIALIZATION ---
init_state()

# --- 3. RENDERING ---
render_header()
render_input()
render_tasks()
