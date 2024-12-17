from collections import defaultdict

class AccountGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, from_account, to_account):
        self.graph[from_account].append(to_account)

    def get_connected_accounts(self, account_id):
        return self.graph[account_id]
