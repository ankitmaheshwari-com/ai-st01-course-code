# kpis.py
import streamlit as st


def display_kpis(df):
    total_rev = df["Revenue"].sum()
    total_orders = df.shape[0]
    avg_order = df["Revenue"].mean()

    # Layout
    st.subheader("Key Metrics")
    c1, c2, c3 = st.columns(3)

    c1.metric("Total Revenue", f"${total_rev:,.0f}")
    c2.metric("Total Orders", total_orders)
    c3.metric("Avg Order Value", f"${avg_order:,.0f}")

    st.markdown("---")
