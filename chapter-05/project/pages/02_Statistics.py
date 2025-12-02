# pages/02_Statistics.py

import streamlit as st
import pandas as pd
from utils import get_data

st.set_page_config(page_title="Statistics", layout="wide")

st.title("📈 Summary Statistics")

df = get_data()

st.success(f" Successfully loaded data with {df.shape[0]} rows!")

st.markdown("### Basic Information")

# 1. Create two equal width columns
col1, col2 = st.columns(2)

# 2. Add placeholders to verify structure
with col1:
    st.write("**Shape**")
    st.write(f"{df.shape[0]} rows × {df.shape[1]} columns")

    st.write("**Column Names**")
    st.write(list(df.columns))

with col2:
    st.write("**Data Types**")

    # Create a nice dataframe for display
    dtypes_df = pd.DataFrame({"Column": df.columns, "Type": df.dtypes.astype(str)})

    st.dataframe(dtypes_df)


st.markdown("### Numerical Summary (describe)")

st.write(df.describe())

st.markdown("### Missing Values (per column)")

missing = df.isnull().sum()
# st.write(missing)

missing_df = pd.DataFrame(
    {
        "Column": missing.index,
        "Missing Values": missing.values,
        "% Missing": (missing / len(df) * 100).round(2),
    }
)

st.dataframe(missing_df)
