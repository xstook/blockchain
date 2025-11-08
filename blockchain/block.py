import hashlib
from datetime import datetime


class Block:
	def __init__(self, index, data, prev_block):
		self.timestamp = datetime.now().strftime("%b-%d-%Y_%H:%M:%S")
		self.index = index
		self.data = data
		self.this_hash = ""
		self.prev_hash = ""
		self.nonce = 0
		self.difficulty = 4
		self.next_block = None
		self.prev_block = prev_block


	def generate_hash(self):
		hash_object = hashlib.sha256()
		hash_object.update(self.timestamp.encode("utf-8"))
		hash_object.update(self.data.encode("utf-8"))
		hash_object.update(self.prev_hash.encode("utf-8"))
		hash_object.update(self.nonce.to_bytes(4, "big"))
		hash_object.update(self.index.to_bytes(4, "big"))
		hash_object.update(self.difficulty.to_bytes(4, "big"))
		return hash_object.hexdigest()


	def mine(self):
		self.nonce = 0
		self.prev_hash = self.prev_block.this_hash
		while not self.this_hash.startswith("0" * self.difficulty):
			self.this_hash = self.generate_hash()
			self.nonce += 1

		self.nonce -= 1


