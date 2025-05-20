import json

def get_transactions(user_id):
    # In real system, connect to Plaid here
    with open("data/transactions.json") as f:
        return json.load(f)
