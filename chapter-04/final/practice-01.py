import streamlit as st

 # Initialize count in Session State (only runs once)
if "count" not in st.session_state:
    st.session_state.count = 0

# Button increases the count
if st.button("Add 1"):
    st.session_state.count = st.session_state.count + 1

# Display the count
st.write(f"Count: {st.session_state.count}")
