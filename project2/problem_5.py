import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev = None

    def calc_hash(self):
        sha = hashlib.sha256()

        information = "|".join([str(self.timestamp), self.data, self.previous_hash]).encode("utf-8")

        sha.update(information)

        return sha.hexdigest()

    def __str__(self):
        return f"(\n\t" + \
               f"data: {self.data}" + \
               f"\n\ttimestamp: {self.timestamp}" + \
               f"\n\tprevious_hash: {self.previous_hash}" + \
               f"\n\thash: {self.hash}" + \
               f"\n)"


class Blockchain:

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def append(self, data):
        if self.is_empty():
            self.head = Block(datetime.utcnow(), data, "0")

        else:
            current_head = self.head
            self.head = Block(datetime.utcnow(), data, current_head.hash)
            self.head.prev = current_head

        self.size += 1

    def is_valid(self):
        node = self.head
        while node:
            if node.prev is None and node.previous_hash != "0":
                return False
            if node.prev is not None and (
                    node.prev.calc_hash() != node.prev.hash or node.previous_hash != node.prev.hash):
                return False
            node = node.prev

        return True

    def __str__(self):
        string = ""
        node = self.head
        while node:
            string = str(node) + string
            if node.prev:
                string = " << " + string
            node = node.prev
        return string


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
blockchain = Blockchain()
blockchain.append("block 0")
blockchain.append("block 1")
blockchain.append("block 2")

print(blockchain)

assert blockchain.is_valid() is True
print("Above blockchain is valid")

blockchain.head.previous_hash = "corrupted"

print(blockchain)

assert blockchain.is_valid() is False
print("Above blockchain is invalid due to corrupted block 2")

# Test Case 2

# Test Case 3
