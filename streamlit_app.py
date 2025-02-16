import streamlit as st
import pandas as pd

# Initialize session state if not already present
if "scores" not in st.session_state:
    st.session_state.scores = [
        {"name": "Josh", "Pushups": 10, "Situps": 20},
    ]


def new_scores():
    """Function to add new scores to the session state"""
    st.session_state.scores.append(
        {
            "name": st.session_state.name,
            "Pushups": st.session_state.pushups,
            "Situps": st.session_state.situps,
        }
    )
    st.experimental_rerun()  # Force UI update


st.write("# Score Table")

# Convert session state data to a DataFrame
score_df = pd.DataFrame(st.session_state.scores)
score_df["Total Points"] = score_df["Pushups"] + score_df["Situps"]

st.dataframe(score_df)  # Use `st.dataframe()` for better table formatting

st.write("# Add a New Score")

# Form for new score submission
with st.form("new_score", clear_on_submit=True):
    name = st.text_input("Name", key="name")
    pushups = st.number_input("Pushups", key="pushups", step=1, value=0, min_value=0)
    situps = st.number_input("Situps", key="situps", step=1, value=0, min_value=0)
    submitted = st.form_submit_button("Submit", on_click=new_scores)
