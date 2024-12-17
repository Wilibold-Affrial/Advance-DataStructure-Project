import streamlit as st
from backend.services.transaction_service import process_transaction

def render():
    st.title("Transactions")
    st.write("Transfer money between accounts.")

    sender_id = st.text_input("Sender Account ID")
    recipient_id = st.text_input("Recipient Account ID")
    amount = st.number_input("Amount to Transfer", min_value=1.0)

    if st.button("Submit Transaction"):
        result = process_transaction(sender_id, recipient_id, amount)
        st.success(result)
