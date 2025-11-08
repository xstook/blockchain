import json
from blockchain.block import Block


class Chain:
	def __init__(self):
		self.genesis_block = Block(0, "", None)
		self.genesis_block.this_hash = "0000000000000000000000000000000000000000000000000000000000000000"
		self.tail_block = self.genesis_block
		self.total_blocks = 0


	def add_block(self, data):
		self.total_blocks += 1
		block = Block(self.total_blocks, data, self.tail_block)
		self.tail_block.next_block = block
		self.tail_block = block
		block.mine()


	def validate(self, start_block=None):
		block = start_block
		if block == None:
			block = self.genesis_block.next_block
		while block != None:
			if block.generate_hash() != block.this_hash:
				return False
			block = block.next_block

		return True


	def print(self):
		print("Total Blocks: {}".format(self.total_blocks))
		block = self.genesis_block.next_block
		while block != None:
			print("Block {}".format(block.index))
			print("    Time  {}".format(block.timestamp))
			print("    Data  {}".format(block.data))
			print("    Hash  {}".format(block.this_hash))
			print("    Prev  {}".format(block.prev_hash))
			print("    Nonc  {}".format(block.nonce))
			print("    Diff  {}".format(block.difficulty))
			print("")
			block = block.next_block


	def save(self, file_name):
		with open(file_name, "w") as f:
			json.dump(self, f, cls=ChainJSONEncoder, indent=4)


	def read(self, file_name):
		with open(file_name, "r") as f:
			self.genesis_block.next_block = None
			self.tail_block = self.genesis_block
			self.total_blocks = 0

			lst = json.load(f)
			for item in lst:
				self.total_blocks += 1
				block = Block(item["index"], item["data"], self.tail_block)
				block.timestamp = item["timestamp"]
				block.this_hash = item["this_hash"]
				block.prev_hash = item["prev_hash"]
				block.nonce = item["nonce"]
				block.difficulty = item["difficulty"]
				self.tail_block.next_block = block
				self.tail_block = block



class ChainJSONEncoder(json.JSONEncoder):
	def default(self, obj):
		encoded = list()

		block = obj.genesis_block.next_block
		while block != None:
			block_encoded = dict()
			block_encoded["timestamp"] = block.timestamp
			block_encoded["index"] = block.index
			block_encoded["data"] = block.data
			block_encoded["this_hash"] = block.this_hash
			block_encoded["prev_hash"] = block.prev_hash
			block_encoded["nonce"] = block.nonce
			block_encoded["difficulty"] = block.difficulty
			encoded.append(block_encoded)
			block = block.next_block

		return encoded


