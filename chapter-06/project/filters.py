# filters.py
import streamlit as st
import pandas as pd


def display_filters(df):
    st.sidebar.header("Filters")

    # Category Filters
    categories = st.sidebar.multiselect(
        "Select Category(s)", df["Category"].unique(), default=df["Category"].unique()
    )

    if categories:
        return df[df["Category"].isin(categories)]

    return df
