import streamlit as st


st.title("Display Commands Demo")
st.header("This is a header")
st.subheader("This is a subheader")

st.write("st.write() can display:")
st.write("Text, numbers:", 42, "and lists:", [1, 2, 3])


age = st.number_input("Enter your age", value=18)
if st.button("Submit"):
    st.write(f"You are {age} years old!")