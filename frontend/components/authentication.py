import streamlit as st
from backend.core.security.encryption import encrypt

# A mock database of user credentials for demonstration purposes
USER_CREDENTIALS = {
    "admin": encrypt("password123", 5),
    "user1": encrypt("securepass", 5),
}

def login():
    st.title("Welcome to the Advanced Banking System")
    st.markdown("Please log in to access your account.")

    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password", key="password")

    if st.button("Log In"):
        encrypted_password = encrypt(password, 5)
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == encrypted_password:
            st.success(f"Welcome, {username}!")
            return True
        else:
            st.error("Invalid username or password.")

    return False
