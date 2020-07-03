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
        self.chain = [] # The blockchain
        self.unconfirmed = [] # Yet-to-be confirmed transactions
        self.initialize()

    def initialize(self):
        """
        A function to create the initial block in the chain.
        """
        initialBlock = Block(0, [], time.time(), "0")
        initialBlock.hash = initialBlock.computeHash()
        self.chain.append(initialBlock)

    @property
    def lastBlock(self):
        """
        A getter function for the last block in the chain.
        """
        return self.chain[-1]

    def proofOfWork(self, block):
        """
        This function tries different nonces to find a fitting hash.
        :param block: The block whose nonce is to be verified.
        """
        block.nonce = 0
        blockHash = block.computeHash()
        while not blockHash.startswith('0' * BlockChain.difficulty):
            block.nonce += 1
            blockHash = block.computeHash()

        return blockHash
    
    def verifyProof(self, block, proof):
        """
        Check if block_hash is valid hash of block and satisfies
        the difficulty criteria.
        """
        return (proof.startswith('0' * BlockChain.difficulty) and
                proof == block.computeHash())

    def addBlock(self, block, proof):
        """
        This function adds a block to the chain by proof of work.
        :param block: The block that is to be added.
        :param proof: The proof of work for the block being added.
        """
        prevBlock = self.lastBlock.hash
        
        if prevBlock != block.prevBlock:
            return False

        if not BlockChain.verifyProof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    def addTransaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        """
        This function serves as an interface to add the pending
        transactions to the blockchain by adding them to the block
        and figuring out proof of work.
        """
        if not self.unconfirmed_transactions:
            return False

        lastBlock = self.lastBlock

        newBlock = Block(index=lastBlock.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=lastBlock.hash)

        proof = self.proofOfWork(newBlock)
        self.add_block(newBlock, proof)
        self.unconfirmed_transactions = []
        return newBlock.index