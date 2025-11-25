import streamlit as st

#  # Initialize count in Session State (only runs once)
if "count" not in st.session_state:
    st.session_state.count = 0

# Button increases the count
if st.button("Add 1"):
    st.session_state.count = st.session_state.count + 1

# Display the count
st.write(f"Count: {st.session_state.count}")



# practice 2
# counter APP

st.title("counter app")

if 'count' not in st.session_state:
    st.session_state.count = 0


col1, col2, col3 = st.columns(3)

with col1:
    if st.button("- subtract"):
        st.session_state.count -=1

with col2:
    if st.button("reset"):
        st.session_state.count = 0

with col3:
    if st.button("+add"):
        st.session_state.count +=1
    
st.header(f"counter : {st.session_state.count}")


# practice 3
# callback


st.title("callback demo")

def calculate_change():
    st.session_state.total = st.session_state.price * st.session_state.quantity


if "total" not in st.session_state:
    st.session_state.total = 0

st.number_input("price", min_value=0.0, value=0.0, key = "price", on_change=calculate_change)
st.number_input("quantity", min_value=0, value = 0, key = "quantity", on_change=calculate_change)

st.success(f"total: {st.session_state.total:.2f}")