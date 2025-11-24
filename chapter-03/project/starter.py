import streamlit as st

st.title("Loan Eligibility Checker (Form Demo)")
st.write("This project demonstrates how to use **forms in Streamlit** for grouped user inputs and submit handling.")



# ------------------------------
# FORM START
# ------------------------------





# ------------------------------
# Loan Eligibility Logic
# ------------------------------
# def check_eligibility(income, credit_score, loan_amount, loan_tenure):
#     min_income = loan_amount * 3
#     min_credit_score = 650
    
#     if income >= min_income and credit_score >= min_credit_score:
#         return True
#     return False




# ------------------------------
# FORM SUBMISSION RESULT
# ------------------------------


import streamlit as st

# -------------------------------------------------
# GitHub Profile README Generator - Starter File
# Chapter 3 Practice Project
# -------------------------------------------------

st.title("GitHub Profile Generator (Starter)")

# Create a two-column layout

# Left column: Form
# Right column: Preview of the generated README

# Inside left column, create a form:
# with st.form("profile_form"):

# Add text inputs for:
# - Name
# - Bio
# - GitHub username

# Add a text input for skills (comma-separated)
# Example: Python, JavaScript, Streamlit

# Add a checkbox asking if user wants to include social links
# If checked → show two more inputs inside the form:
# - LinkedIn URL (optional)
# - Twitter URL (optional)

# Add a submit button for the form

# After form is submitted:
# - Generate the README markdown as a string
# - Show the generated markdown in the right column
#   using st.markdown()
