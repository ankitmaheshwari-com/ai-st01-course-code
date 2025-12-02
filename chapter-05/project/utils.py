# utils.py

import streamlit as st
import pandas as pd


def load_csv(uploaded_file):
    """Safely reads a CSV file into a DataFrame."""
    try:
        df = pd.read_csv(uploaded_file)
        return df
    except Exception:
        st.error("Error reading the CSV file. Please check the file format.")
        st.stop()


def get_data():
    """
    Returns the dataframe from session_state.
    If not found, stops the app with a message.
    """
    if "df" not in st.session_state:
        st.info("No CSV loaded yet. Please upload a file on the Home page.")
        st.stop()

    return st.session_state["df"]
