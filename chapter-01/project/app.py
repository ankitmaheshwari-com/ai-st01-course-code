import streamlit as st
import random

# --- List of motivational quotes ---
QUOTES = [
    "The best way to get started is to quit talking and begin doing. — Walt Disney",
    "Success is not final; failure is not fatal: It is the courage to continue that counts. — Winston Churchill",
    "Don’t let yesterday take up too much of today. — Will Rogers",
    "If you are working on something that you really care about, you don’t have to be pushed. The vision pulls you. — Steve Jobs",
    "It’s not whether you get knocked down, it’s whether you get up. — Vince Lombardi",
    "People who are crazy enough to think they can change the world are the ones who do. — Rob Siltanen",
    "The only limit to our realization of tomorrow is our doubts of today. — Franklin D. Roosevelt",
]

# Streamlit page setup
st.set_page_config(page_title="Motivation Generator")

st.title(" Random Motivational Quote Generator")
st.write("Click the button to get inspired!")

# Button to show a new quote
if st.button(" Give me motivation!"):
    st.write(random.choice(QUOTES))
else:
    st.write("Press the button to receive motivation.")



