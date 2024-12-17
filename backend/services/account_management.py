from backend.core.data_structures.hash_table import HashTable

accounts_db = HashTable()

def create_account(account_id, account_details):
    accounts_db.insert(account_id, account_details)

def get_account_details(account_id):
    return accounts_db.search(account_id)
