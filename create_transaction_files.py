import json
import os

# The transaction data
transaction_data = [
  {"date": "2024-05-01", "amount": 5000, "description": "Grocery Store"},
  {"date": "2024-05-02", "amount": 15000, "description": "Crypto Investment"},
  {"date": "2024-05-03", "amount": 12000, "description": "Online Casino"}
]

def create_transaction_files():
    # Get current directory
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")
    
    # Create the file in several possible locations
    locations = [
        "transactions.json",  # Current directory
        "data/transactions.json",  # data subfolder
        "agents/tools/data/transactions.json",  # Original path
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "transactions.json"),  # Same directory as script
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/transactions.json")  # data subfolder relative to script
    ]
    
    for location in locations:
        try:
            # Ensure directory exists
            directory = os.path.dirname(location)
            if directory and not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
                
            # Create the file
            with open(location, 'w') as f:
                json.dump(transaction_data, f, indent=2)
            print(f"✅ Successfully created file at: {os.path.abspath(location)}")
        except Exception as e:
            print(f"❌ Failed to create file at {location}: {e}")
    
    print("\nNow try running your transaction analyzer again!")

if __name__ == "__main__":
    create_transaction_files()