import doctest
import json

from hashlib import sha256


class Block:
    def __init__(self, index, transactions, timestamp, prev_block):
        """
        Constructor for the `Block` class.
        :param index: Index of the block.
        :param transactions: List of block's transactions.
        :param timestamp: Time when block was created.
        :param prev_block: The hash of the previous block in the chain
        """
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.prev_block = prev_block

    def calc_hash(self):
        """
        This function calculates the hash of the block and return a hashed json object
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
