import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.prev = None
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()

        sha.update(self.data.encode('utf-8'))

        return sha.hexdigest()


class Blockchain:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def append(self, block):
        if self.size == 0:
            block.prev = None
            block.next = None
            block.previous_hash = None
            self.head = block
            self.tail = block

        elif self.size == 1:
            self.tail = block
            self.tail.prev = self.head
            self.tail.previous_hash = self.head.hash
            self.head.next = self.tail

        else:
            current_tail = self.tail
            self.tail = block
            self.tail.prev = current_tail
            self.tail.previous_hash = current_tail.hash
            current_tail.next = self.tail

        self.size += 1


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3