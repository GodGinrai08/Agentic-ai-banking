import json
import os

def load_transactions(_input=None):
    path = os.path.join(os.path.dirname(__file__), "transactions.json")
    with open(path, "r") as f:
        data = json.load(f)
    return {"transactions": data}
