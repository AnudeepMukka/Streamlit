import streamlit as st
import pandas as pd
import os
from datetime import datetime

# File to store application data
import os




# Load existing data if the file exists

app_df = pd.read_csv("Application Tracker.csv")


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
    pd.DataFrame(st.session_state.applications).to_csv("Application Tracker.csv", index=False)
    
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
