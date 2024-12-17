from backend.services.account_management import get_account_details
from backend.core.data_structures.avl_tree import AVLTree

account_tree = AVLTree()

def generate_account_summary(account_id):
    account_details = get_account_details(account_id)
    if account_details:
        return {
            "Account ID": account_id,
            "Name": account_details["name"],
            "Balance": account_details["balance"],
        }
    return None
