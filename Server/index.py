import time
import json

from Server import BlockChain
from flask import Flask, request

# Setup the blockchain
blockchain = BlockChain()
blockchain.initialize()

# Create a Flask app
app = Flask(__name__)

# Process routes
# New transaction
@app.route("/new_transaction", methods=["POST"])
def new_transaction():
    user_data = request.get_json()
    required_fields = ["author", "content"]

    for field in required_fields:
        if not user_data.get(field):
            return "Invalid request for making a transaction", 404

    user_data["timestamp"] = time.time()

    blockchain.add_transaction(user_data)

    return "Success", 201
