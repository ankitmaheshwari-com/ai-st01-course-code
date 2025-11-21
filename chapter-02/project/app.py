import streamlit as st

# Title of the Landing Page
st.title("A Simple Landing Page")

# Hero Section: Large text with a short description
st.markdown("""
    ## Your Business Name
    A brief tagline or description about what you offer.
    *"Providing solutions that matter."*
""")

# Sidebar Navigation
st.sidebar.title("Navigation")
st.sidebar.write("Choose a section:")
option = st.sidebar.radio("Go to", ["Home", "Features", "FAQ"])

# Display different content based on the sidebar selection
if option == "Home":
    st.header("Home")
    st.write("Welcome to our landing page. Scroll down to learn more about our product features.")
elif option == "Features":
    st.header("Features")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Feature 1")
        st.write("Description of the first feature.")
    with col2:
        st.subheader("Feature 2")
        st.write("Description of the second feature.")
elif option == "FAQ":
    st.header("Frequently Asked Questions")
    with st.expander("What is this service about?"):
        st.write("This is a detailed answer to the first FAQ.")
    with st.expander("How can I sign up?"):
        st.write("Here is how you can sign up for our service.")
    with st.expander("What are the prices?"):
        st.write("We offer various pricing models depending on your needs.")

# Success Toast Message or Banner
st.success("Successfully loaded the page!")


