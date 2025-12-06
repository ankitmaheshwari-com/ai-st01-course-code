# data_loader.py
import pandas as pd
import streamlit as st


def load_data(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file)
        df["Date"] = pd.to_datetime(df["Date"])
        return df

    except Exception as e:
        st.error(f"Error: {e}")
        st.stop()
