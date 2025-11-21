import streamlit as st
print(">>> Script running!") # Watch your terminal

number = st.number_input("Pick a number", value=5)
st.write(f"Your number doubled is: {number * 2}")