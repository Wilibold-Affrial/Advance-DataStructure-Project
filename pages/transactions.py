import streamlit as st

def render_transactions():
    st.title("Transactions")
    st.write("View and manage your transactions here.")
    # Placeholder for transaction data
    transactions = [
        {"Date": "2024-12-15", "Amount": "$1,000", "Type": "Credit"},
        {"Date": "2024-12-14", "Amount": "$500", "Type": "Debit"},
    ]
    st.table(transactions)
