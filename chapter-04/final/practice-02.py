import streamlit as st

# Widget Keys Auto-Create Session State

# without key parameter
name = st.text_input("enter name")  #name is just local variable
# with key parameter
name = st.text_input("enter name", key = "username") #automatically create session variable "username"





# Callbacks 

def add_one():
    st.session_state.count +=1

if "count" not in st.session_state:
    st.session_state.count = 0
st.button("add", on_click=add_one)
st.write(f"count : {st.session_state.count}")






# callback with parameter
st.title("Callback Parameters Demo")

# Initialize
if "messages" not in st.session_state:
    st.session_state.messages = []

# Callback with args
def add_message(text, priority):
    st.session_state.messages.append({"text": text,"priority": priority})


col1, col2 = st.columns(2)
with col1:
    st.button("Add Normal", on_click=add_message,
    args=("Normal message", "low"))

with col2:
    st.button("Add Urgent", on_click=add_message,
    args=("Urgent message", "high"))

# Display messages
for msg in st.session_state.messages:
    if msg["priority"] == "high":
        st.error(msg["text"])
    else:
        st.info(msg["text"])

