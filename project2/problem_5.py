import hashlib
from datetime import datetime


class Block:

    def __init__(self, timestamp, data, previous_hash="0"):
        if timestamp is None or data is None or previous_hash is None:
            raise ValueError("timestamp, data and previous_hash MUST NOT be None")

        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev = None

    def calc_hash(self):
        sha = hashlib.sha256()

        block_content = "|".join([str(self.timestamp), self.data, self.previous_hash]).encode("utf-8")

        sha.update(block_content)

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
            self.head = Block(datetime.utcnow(), data)

        else:
            current_head = self.head
            self.head = Block(datetime.utcnow(), data, current_head.hash)
            self.head.prev = current_head

        self.size += 1

    def length(self):
        return self.size

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
print("\n" + "_"*90)
print("\n1. Test Blockchain creation, length and validity")
blockchain = Blockchain()
blockchain.append("block 0")
blockchain.append("block 1")
blockchain.append("block 2")

print()
print(blockchain)

assert blockchain.length() == 3
print("\nBlockchain length == 3")

assert blockchain.is_valid() is True
print("\nAbove blockchain is valid")

blockchain.head.previous_hash = "corrupted"

print()
print(blockchain)

assert blockchain.is_valid() is False
print("\nAbove blockchain is invalid due to corrupted block 2")

# Test Case 2
print("\n" + "_"*90)
print("\n2. Test Block creation and hash calculation")
block = Block(timestamp=datetime(2023, 11, 1, 15, 00, 00), data="test", previous_hash="0")

print(f"\nCreating block with timestamp = 2023-11-01 15:00:00, data = test and previous_hash = 0:")

print(block)

assert block.data == "test"
assert str(block.timestamp) == "2023-11-01 15:00:00"
assert block.previous_hash == "0"
assert block.hash == "3d3fa9b37eaa8b41bea3ed874331a04147b0f4cdcf4b6ab5653b69e5c23548dd"

print("Creation and hash calculation were successful")

# Test Case 3
print("\n" + "_"*90)
print("\n3. Test Block creation with null values")
print("\nCreating Block with timestamp=None...")
try:
    block = Block(timestamp=None, data="test", previous_hash="0")
except ValueError:
    print("ValueError exception thrown, as expected")

print("\nCreating Block with data=None...")
try:
    block = Block(timestamp=datetime(2023, 11, 1, 15, 00, 00), data=None, previous_hash="0")
except ValueError:
    print("ValueError exception thrown, as expected")

print("\nCreating Block with previous_hash=None...")
try:
    block = Block(timestamp=datetime(2023, 11, 1, 15, 00, 00), data="test", previous_hash=None)
except ValueError:
    print("ValueError exception thrown, as expected")

# Test Case 4
print("\n" + "_"*90)
print("\n4. Test appending null values to Blockchain")

print("\nTrying blockchain.append(None)...")
try:
    blockchain = Blockchain()
    blockchain.append(None)
except ValueError:
    print("ValueError exception thrown, as expected")
