import streamlit as st

def render_support_tickets():
    st.title("Support Tickets")
    st.write("Submit and view support tickets.")
    # Ticket submission form
    subject = st.text_input("Subject")
    description = st.text_area("Description")
    if st.button("Submit Ticket"):
        st.success("Your ticket has been submitted!")
    # Placeholder for existing tickets
    tickets = [
        {"ID": 1, "Subject": "Unable to login", "Status": "Resolved"},
        {"ID": 2, "Subject": "Transaction issue", "Status": "Pending"},
    ]
    st.table(tickets)
