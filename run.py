#!/usr/bin/python3

from blockchain.block import Block
from blockchain.chain import Chain


def main():
	# Create and save a chain to file
	print("Creating a chain")
	chain = Chain()
	chain.add_block("First")
	chain.add_block("Second")
	chain.add_block("Third")
	chain.add_block("Fourth")
	chain.save("chain.json")
	chain.print()
	print("Valid: {}".format(chain.validate()))

	print("")

	# Load the chain from file
	print("Loading a chain")
	chain = Chain()
	chain.read("chain.json")
	chain.print()
	print("Valid: {}".format(chain.validate()))




if __name__ == "__main__":
	main()
