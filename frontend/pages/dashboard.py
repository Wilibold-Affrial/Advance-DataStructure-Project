import streamlit as st
from backend.services.reporting_service import generate_account_summary

def render():
    st.title("Dashboard")
    st.write("Welcome to your Advanced Banking System dashboard!")

    # Fetch account summary
    account_id = st.text_input("Enter your account ID:")
    if st.button("Get Account Summary"):
        summary = generate_account_summary(account_id)
        if summary:
            st.json(summary)
        else:
            st.error("Account not found!")
