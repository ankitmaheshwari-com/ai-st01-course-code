import streamlit as st

# ------------------------------------------------------
# Profile Card – Starter Template
# Students will complete this by adding their own details.
# ------------------------------------------------------

st.set_page_config(page_title="My Profile Card", layout="centered")

# ---- Title Section ----
st.title("My Profile Card")
st.write("Fill in your details below to complete the app!")

# ---- Profile Image (Optional) ----
# TODO: Add an image using st.image()
# Example:
# st.image("my_photo.jpg", width=200)

# ---- Basic Info ----
# TODO: Add your name using st.header()
# TODO: Add your role or title using st.subheader()

# ---- Short Bio ----
# TODO: Add a short introduction using st.write() or st.markdown()

# ---- Skills Section ----
st.markdown("### Skills")
# TODO: Replace these with your actual skills
skills = [
    "Python",
    "Streamlit",
    "Data Analysis"
]

# Display skills (Students can change layout later)
for skill in skills:
    st.write(f"• {skill}")

# ---- Social Links ----
st.markdown("### Connect with Me")
# TODO: Add your social links using st.markdown()
# Example:
# st.markdown("[LinkedIn](https://www.linkedin.com/in/your-profile/)")

# ---- Extra (Optional) ----
# TODO: Add a sidebar with additional details like hobbies or location
# st.sidebar.title("More About Me")
# st.sidebar.write("Your content here...")


