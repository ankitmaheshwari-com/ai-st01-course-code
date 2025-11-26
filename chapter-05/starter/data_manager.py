import pandas as pd

# def load_initial_data():
#     """
#     Simulates loading a raw dataset (e.g., from CSV or SQL).
#     For the video, we use a hardcoded list of dictionaries to keep it runnable without external files.
#     """
#     raw_data = [
#         {"id": 101, "text": "The user interface is incredibly intuitive. Loved it!", "source": "Twitter"},
#         {"id": 102, "text": "The load times are terrible on mobile. Needs fixing.", "source": "App Store"},
#         {"id": 103, "text": "It's okay, but the color scheme is a bit jarring.", "source": "Survey"},
#         {"id": 104, "text": "Best investment I made this year. Highly recommend.", "source": "LinkedIn"},
#         {"id": 105, "text": "Customer support never replied to my ticket.", "source": "Email"},
#         {"id": 106, "text": "Can you add a dark mode feature?", "source": "Feature Request"},
#         {"id": 107, "text": "I encountered a bug on the checkout page.", "source": "Bug Report"},
#         {"id": 108, "text": "Streamlit makes python so much fun!", "source": "Twitter"},
#         {"id": 109, "text": "Documentation is a bit sparse in some areas.", "source": "Dev Forum"},
#         {"id": 110, "text": "Five stars! Amazing work.", "source": "App Store"},
#     ]
#     return raw_data

def convert_state_to_dataframe(session_labels):
    """
    Helper to convert the session_state dictionary into a downloadable DataFrame.
    """
    # session_labels is a dict: {item_id: 'Label'}
    data = []
    for item_id, label in session_labels.items():
        data.append({"ID": item_id, "Label": label})
    
    return pd.DataFrame(data)