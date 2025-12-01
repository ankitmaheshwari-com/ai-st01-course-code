import streamlit as st

#  # Initialize count in Session State
if "count" not in st.session_state:
    st.session_state.count = 0

# Button increases the count
if st.button("Add 1"):
    st.session_state.count = st.session_state.count + 1

# Display the count
st.write(f"Count: {st.session_state.count}")



# 2 ways to access session state

# 1. dot notation
st.session_state.count = 5
value = st.session_state.count


# 2. bracket notation
st.session_state["count"] = 5
value = st.session_state["count"]



# Common Dictionary Methods
# returns None if key doesn't exist
value = st.session_state.get("count")

# Return default value if key doesn't exist
value = st.session_state.get("count", 0)


# clearing all session state 
if st.button("clear everything"):
    st.session_state.clear()
    st.rerun()    

# clearing one by one
for key in list(st.session_state.keys()):
    del st.session_state[key]


