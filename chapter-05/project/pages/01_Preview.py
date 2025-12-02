# pages/01_Preview.py

import streamlit as st
from utils import get_data

st.set_page_config(page_title="Data Preview", layout="wide")

st.title("📊 Data Preview")
st.write("This page will show the raw data.")


# 1. Fetch the data securely
df = get_data()

st.success(f" Successfully loaded data with {df.shape[0]} rows!")

# 1. Add a header
st.markdown("### Full Preview (Scrollable Table)")
st.dataframe(df)


st.markdown("### Select Columns to View")
selected_columns = st.multiselect("Choose columns to display.", df.columns.tolist())

st.write(f"You selected: {selected_columns}")

if selected_columns:
    st.write("Showing selected_columns.")
    st.dataframe(df[selected_columns])
else:
    st.info("Select one or more columns from the drop-down to preview them.")
