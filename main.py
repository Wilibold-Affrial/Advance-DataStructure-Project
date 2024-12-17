import streamlit as st
from components.authentication import login, logout
from components.sidebar import render_sidebar
from pages.dashboard import render_dashboard
from pages.transactions import render_transactions
from pages.account_management import render_account_management
from pages.support_tickets import render_support_tickets

# Main Streamlit application
def main():
    st.set_page_config(page_title="Advanced Banking System", layout="wide")

    # User session management
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
        st.session_state["username"] = None

    if not st.session_state["authenticated"]:
        login()
    else:
        render_sidebar()  # Render the navigation sidebar
        page = st.sidebar.selectbox(
            "Navigate", ["Dashboard", "Transactions", "Account Management", "Support Tickets", "Logout"]
        )
        if page == "Dashboard":
            render_dashboard()
        elif page == "Transactions":
            render_transactions()
        elif page == "Account Management":
            render_account_management()
        elif page == "Support Tickets":
            render_support_tickets()
        elif page == "Logout":
            logout()

if __name__ == "__main__":
    main()
