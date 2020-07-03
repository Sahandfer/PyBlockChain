import doctest
import json

from hashlib import sha256


class Block:
    def __init__(self, index, transactions, timeStamp, prevBlock):
        """
        Constructor for the `Block` class.
        :param index: Index of the block.
        :param transactions: List of block's transactions.
        :param timestamp: Time when block was created.
        :param prevBlock: The hash of the previous block in the chain
        """
        self.index = index
        self.transactions = transactions
        self.timeStamp = timeStamp
        self.prevBlock = prevBlock
        self.nonce = nonce

    def computeHash(self):
        """
        This function computes the hash of the block and return a hashed json object
        """
        blockString = json.dumps(self.__dict__, sort_keys=True)
        return sha256(blockString.encode()).hexdigest()
