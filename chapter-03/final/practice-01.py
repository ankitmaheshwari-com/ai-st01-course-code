import streamlit as st

st.title("Forms & Widgets")

# practice 1 | widgets
# -----------------------------------
st.header("Widgets")
name = st.text_input("Your name")
age = st.number_input("Your age", min_value=0, max_value=120, value=25)
if st.button("Submit"):
    st.success(f"Hello {name}, you are {age} years old!")


# practice 2 | checkBox, selectbox| widgets
# ----------------------------------------

st.header("Selection & Slider ")
# Selection
color = st.selectbox("Favorite color", ["Red", "Green", "Blue"])
agree = st.checkbox("I agree to terms")
# Slider
rating = st.slider("Rate this app", 1, 10, 5)
# Display results
st.write(f"Color: {color}")
st.write(f"Agreed: {agree}")
st.write(f"Rating: {rating}/10")


# Basic form structure
# Registration form
# -----------------------------------
st.header("Registration Form")
with st.form("registration"):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    age = st.slider("Age", 18, 100, 25)
    plan = st.selectbox("Plan", ["Free", "Pro", "Enterprise"])
    submitted = st.form_submit_button("Register")

if submitted:
    st.success("Registration successful!")
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Age: {age}")
    st.write(f"Plan: {plan}")
