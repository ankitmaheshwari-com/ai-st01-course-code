import streamlit as st

def render_header(progress, total):
    """Renders the top bar with a progress indicator."""
    st.title("Human-in-the-Loop Labeler")
    
    # Calculate percentage
    pct = progress / total
    st.progress(pct)
    st.caption(f"Progress: {progress}/{total} items labeled")

def render_item_card(item, current_label):
    """
    Displays the actual data item to be labeled.
    """
    # Create a nice container (Card view)
    with st.container(border=True):
        st.subheader(f"Item #{item['id']}")
        st.info(item['text'], icon="📝")
        st.caption(f"Source: {item['source']}")
        
        # Visual feedback if it's already labeled
        if current_label:
            st.success(f"Current Label: **{current_label}**")
        else:
            st.warning("Status: Unlabeled")

def render_sidebar_metrics(labels_dict):
    """
    Shows statistics in the sidebar.
    """
    st.sidebar.header("Session Metrics")
    st.sidebar.write(f"Total Labeled: **{len(labels_dict)}**")
    st.sidebar.write(labels_dict) # Debug view