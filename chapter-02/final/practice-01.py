
import streamlit as st

st.title("Chapter 2")
st.header("Understanding Display Commands")
st.subheader("Using Titles, Headers, and Subheaders")


# Markdown
st.markdown("**Bold text**")
st.markdown("*italic*")
st.markdown("`inline code`")



# Status messages
st.success("Operation completed successfully!")
st.warning("This is a warning message.")
st.error("error message.")
st.info("some general information.")


if st.button("send mssg"):
    st.toast("mssg sent!!!")

# Sidebar
st.sidebar.title("Sidebar Section")
st.sidebar.write("This is inside the sidebar.")

# Columns
col1, col2= st.columns(2)
col1.write("Column 1")
col2.write("Column 2")

# container
with st.container():
    st.header("Container Demo")
    st.write("Everything you see here is part of the same container.")
    st.success("This success message is also inside the container.")



# Expander
with st.expander("More Details"):
    st.write("text is hidden until expanded.")

# Tabs
tab1, tab2 = st.tabs(["Overview", "Details"])
tab1.write("overview section.")
tab2.write("detailed section.")
