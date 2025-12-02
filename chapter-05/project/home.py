# Home.py
import streamlit as st
from utils import load_csv

# 1. Configure the page
st.set_page_config(page_title="CSV Data Analyzer", layout="wide")

# 2. Add Title and Description
st.title("📊 CSV Data Analyzer")
st.write("Upload a CSV file to explore it across the different pages.")

st.markdown("### Step 1: Upload Your CSV")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv", "tsv"])

if uploaded_file is not None:
    df = load_csv(uploaded_file)
    st.session_state["df"] = df

    st.success("File uploaded and data loaded successfully! ✅")

    # 1. Show basic metadata
    st.markdown("### Quick Overview")
    st.write(f"**File name:** `{uploaded_file.name}`")
    st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")

    # 2. Show a small sample (first 5 rows)
    st.markdown("### Sample Preview")
    st.dataframe(df.head())

    # 3. Guide the user
    st.info("👈 Use the sidebar menu to access advanced analysis pages.")

else:
    st.info(" Please upload a CSV file to get started!")
