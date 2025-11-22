import streamlit as st

st.set_page_config(page_title="Profile Summary App")

st.title("Profile Summary App")

# Sidebar inputs
name = st.sidebar.text_input("Enter your name")
age = st.sidebar.number_input("Enter your age", min_value=0, value=18)
profession = st.sidebar.text_input("Enter your profession")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.header("Basic Information")
    st.write(f"**Name:** {name if name else 'Not provided'}")
    st.write(f"**Age:** {age}")
    st.write(f"**Profession:** {profession if profession else 'Not provided'}")

with col2:
    st.header("About You")
    st.write("This is where additional details or skills could be shown.")
    st.write("- Skill 1")
    st.write("- Skill 2")
    st.write("- Skill 3")

# Status message based on age
if age < 18:
    st.warning("You are under 18.")
else:
    st.success("You are eligible!")

# Expander
with st.expander("Additional Notes"):
    st.write("hobbies, goals, etc.")
