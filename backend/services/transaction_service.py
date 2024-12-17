from backend.services.account_management import get_account_details
from backend.core.data_structures.account_graph import AccountGraph

account_graph = AccountGraph()

def process_transaction(sender_id, recipient_id, amount):
    sender = get_account_details(sender_id)
    recipient = get_account_details(recipient_id)

    if not sender or not recipient:
        return "Invalid accounts!"

    if sender["balance"] < amount:
        return "Insufficient balance!"

    # Deduct and Add Balance
    sender["balance"] -= amount
    recipient["balance"] += amount

    # Log transaction in the graph
    account_graph.add_edge(sender_id, recipient_id)

    return f"Transaction of ${amount} from {sender_id} to {recipient_id} completed!"
