# app.py
import streamlit as st
import pandas as pd
from data_loader import load_data
from filters import display_filters
from kpis import display_kpis
from charts import display_charts

# 1. Page Configuration
st.set_page_config(page_title="Sales Dashboard", layout="wide", page_icon="📊")

# 2. Main Title
st.title("📊 Business Sales Dashboard")

# 3 Sidebar
st.sidebar.header("Configuration")
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)

    if not df.empty:
        st.sidebar.success("Data loaded successfully.")

        df_filtered = display_filters(df)
        st.sidebar.write(f"Showing {len(df_filtered)} rows")

        # st.dataframe(df_filtered.head())

        # KPIs
        display_kpis(df_filtered)

        # Charts
        display_charts(df_filtered)

        # Raw Data
        with st.expander("📂 View Underlying Data"):
            st.dataframe(
                df_filtered.sort_values(by="Date", ascending=False),
                use_container_width=True,
            )

    else:
        st.error("File is empty or invalid.")

else:
    st.sidebar.info(" Please upload a file. ")
