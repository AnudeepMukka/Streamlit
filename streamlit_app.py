import streamlit as st
import pandas as pd
import os
from datetime import datetime

# File to store application data
import os

# Get the user's Downloads directory
home_dir = os.path.expanduser("~")
FILE_PATH = os.path.join(home_dir, "Downloads", "Application Tracker.csv")


# Load existing data if the file exists
if os.path.exists(FILE_PATH):
    app_df = pd.read_csv(FILE_PATH)
else:
    app_df = pd.DataFrame(columns=["Date", "Company", "Role", "POC", "Status"])

# Convert DataFrame to session state
if "applications" not in st.session_state:
    st.session_state.applications = app_df.to_dict(orient="records")

def new_application():
    """Function to add a new application and save to CSV"""
    new_entry = {
        "Date": st.session_state.date,
        "Company": st.session_state.company,
        "Role": st.session_state.role,
        "POC": st.session_state.poc,
        "Status": st.session_state.status,
    }
    
    st.session_state.applications.append(new_entry)
    
    # Save to CSV
    pd.DataFrame(st.session_state.applications).to_csv(FILE_PATH, index=False)
    
    st.rerun()

st.write("# Application Tracker")

# Convert session state data to a DataFrame
app_df = pd.DataFrame(st.session_state.applications)

st.dataframe(app_df)

st.write("# Add a New Application")

# Form for new application submission
with st.form("new_application", clear_on_submit=True):
    date = st.date_input("Date of Application", value=datetime.today(), key="date")
    company = st.text_input("Company", key="company")
    role = st.text_input("Role", key="role")
    poc = st.text_input("Point of Contact (POC)", key="poc")
    status = st.selectbox("Status", ["Applied", "Interview", "Offer", "Rejected"], key="status")
    submitted = st.form_submit_button("Submit", on_click=new_application)
