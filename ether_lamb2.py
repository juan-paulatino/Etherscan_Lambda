import json
import requests

def get_etherscan_data():
    url = "https://api.etherscan.io/api"  # Etherscan API URL
    api_key = "TGZD8UFBJHXHQ55ZIU2TT8MD9Z8BUFTH7M"  # Replace with your Etherscan API Key

    # Define the parameters for the API request
    parameters = {
        "module": "account",
        "action": "balance",
        "addre ss": "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae",  # Replace with the Ethereum address
        "tag": "latest",
        "apikey": api_key
    }

    # Send a GET request to the Etherscan API
    response = requests.get(url, params=parameters)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()

        # Convert the balance from Wei to Ether
        balance_in_ether = int(data['result']) / (10 ** 18)

        # Return the balance
        return f"Balance: {balance_in_ether} Ether"

def lambda_handler(event, context):
    # Call the get_etherscan_data function
    balance = get_etherscan_data()
    
    # Return a response with a status code and the balance in the body
    return {
        'statusCode': 200,
        'body': json.dumps({"balance": balance})
    }
