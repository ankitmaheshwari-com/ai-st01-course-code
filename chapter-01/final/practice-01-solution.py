import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Profile Card", layout="centered")

# --- Profile Data ---
NAME = "Name"
BIO = "ML Enthusiast • Coffee Lover"


PROFILE_PIC = (
    # "image.png" your image path
)

SOCIAL_LINKS = {
    "GitHub": "https://github.com",
    "LinkedIn": "https://linkedin.com",
    "Twitter": "https://twitter.com"
}

# --- Title ---
st.title("Profile Card App")

st.write("A simple interactive profile component built with Streamlit.")

# --- Profile Card ---
with st.container():
    st.image(PROFILE_PIC, width=100)

    st.subheader(NAME)
    st.write(BIO)

    # Social links
    st.write("### 🌐 Connect with me")
    cols = st.columns(len(SOCIAL_LINKS))

    for (platform, link), col in zip(SOCIAL_LINKS.items(), cols):
        col.markdown(f"[{platform}]({link})")

    # Button
    if st.button("Say Hi 👋"):
        st.success("Hello! Thanks for visiting the profile.")

# Divider
st.write("---")

# Additional Info Section (optional)
st.write("### About This App")
st.write(
    "This is a simple Profile Card App built using Streamlit. "
    "It demonstrates layout, images, text, markdown, and button interactivity."
)
