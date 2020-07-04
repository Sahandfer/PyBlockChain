import time
import json
import Block

from hashlib import sha256


class BlockChain:
    difficulty = 2  # Difficulty for proof of work

    def __init__(self):
        """
        Constructor for the `Blockchain` class.
        """
        self.chain = []  # The blockchain
        self.pending_transactions = []  # Yet-to-be confirmed transactions (pending)

    def initialize(self):
        """
        A function to create the initial block in the chain.
        """
        initial_block = Block(0, [], time.time(), "0")
        initial_block.hash = initial_block.calc_hash()
        self.chain.append(initial_block)

    @property
    def last_block(self):
        """
        A getter function for the last block in the chain.
        """
        return self.chain[-1]

    def proof_of_work(self, block):
        """
        This function tries different nonces to find a fitting hash.
        :param block: The block whose nonce is to be verified.
        """
        block.nonce = 0
        blockHash = block.computeHash()
        while not blockHash.startswith("0" * BlockChain.difficulty):
            block.nonce += 1
            blockHash = block.calc_hash()

        return blockHash

    def verify_proof_of_work(self, block, proof):
        """
        Check if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        return (
            proof.startswith("0" * BlockChain.difficulty)
            and proof == block.calc_hash()
        )

    def add_block(self, block, proof):
        """
        This function adds a block to the chain by verifying proof of work.
        :param block: The block that is to be added.
        :param proof: The proof of work for the block being added.
        """
        prev_block = self.last_block.hash

        if prev_block != block.prev_block:
            return False

        if not BlockChain.verify_proof_of_work(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine(self):
        """
        This function is for mining pending transactions.
        """
        if not self.pending_transactions:
            return False

        last_block = self.last_block

        new_block = Block(
            index=last_block.index + 1,
            transactions=self.pending_transactions,
            timestamp=time.time(),
            prev_block=last_block.hash,
        )

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.pending_transactions = []
        return new_block.index
