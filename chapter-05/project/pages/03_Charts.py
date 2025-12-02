# pages/03_Charts.py

import streamlit as st
from utils import get_data

st.set_page_config(page_title="Charts", layout="wide")

st.title("📉 Charts & Visualizations")

df = get_data()

st.write(f"Ready to plot data from {df.shape[0]} rows.")

# 1. Filter for numeric columns only

numeric_cols = df.select_dtypes(include="number").columns.tolist()
st.write("Found numeric columns:", numeric_cols)

if not numeric_cols:
    st.info(
        "No numeric columns found in the dataset. Charts are only available for numeric data."
    )
    st.stop()


st.markdown("### Select a Numeric Column to Plot")
selected_col = st.selectbox("Numeric column", numeric_cols)

# 2. Radio button for chart type
chart_type = st.radio("Chart Type", ["Line Chart", "Bar Chart"], horizontal=True)

st.markdown("### Chart")

if chart_type == "Line Chart":
    st.line_chart(df[selected_col])
elif chart_type == "Bar Chart":
    st.bar_chart(df[selected_col])

st.caption("Tip: Try different numeric columns to see how the distribution changes.")
