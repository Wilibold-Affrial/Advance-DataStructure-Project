import streamlit as st

def render_account_management():
    st.title("Account Management")
    st.write("Manage your account settings here.")
    # Example settings
    st.text_input("Update Email")
    st.text_input("Update Phone Number")
    if st.button("Save Changes"):
        st.success("Account information updated!")
