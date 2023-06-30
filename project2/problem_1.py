class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def move_to_head(self, node):
        if self.is_empty():
            print("DoublyLinkedList is empty. Nothing to move. Try adding the node first.")
            return

        if self.head == node:
            return

        if self.tail == node:
            self.tail = node.prev

        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        node.next = self.head
        node.next.prev = node
        node.prev = None
        self.head = node

    def add_to_head(self, node):
        if self.is_empty():
            node.next = None
            node.prev = None
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            node.next.prev = node
            node.prev = None
            self.head = node

        self.size += 1

    def remove_tail(self):
        if self.is_empty():
            print("DoublyLinkedList is empty. Nothing to remove.")
            return None

        key = self.tail.key

        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.tail is not None:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return key

    def is_empty(self):
        return self.size == 0


class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Capacity must be a positive number
        if capacity is None or capacity <= 0:
            raise ValueError("Capacity must be an integer greater than 0")

        # Initialize class variables
        self.cache = {}
        self.queue = DoublyLinkedList()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            self.queue.move_to_head(self.cache[key])
            return self.cache[key].value

        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key is None:
            print("Key is None. Nothing to set.")
            return

        if key not in self.cache:
            if len(self.cache) == self.capacity:
                self.remove_oldest()

            node = Node(key, value)
            self.queue.add_to_head(node)
            self.cache[key] = node

    def remove_oldest(self):
        oldest_key = self.queue.remove_tail()

        if oldest_key is None:
            print("Key is None. Nothing to delete.")
            return

        if oldest_key in self.cache:
            del self.cache[oldest_key]

    def __str__(self):
        return str(self.cache)


print("0. Testing main functionality")

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

assert our_cache.get(1) == 1  # returns 1
assert our_cache.get(2) == 2  # returns 2
assert our_cache.get(9) == -1  # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

assert our_cache.get(3) == -1  # returns -1 because the cache reached its capacity and 3 was the oldest entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print("1. Cache must be instantiated with a capacity greater than 0")

try:
    LRU_Cache(None)  # This should raise a ValueError exception
except ValueError as e:
    assert str(e) == "Capacity must be an integer greater than 0"

try:
    LRU_Cache(-1)  # This should raise a ValueError exception
except ValueError as e:
    assert str(e) == "Capacity must be an integer greater than 0"

# Test Case 2
print("2. Setting an empty key should have no effect and no old values should be deleted at capacity in that case")

test_cache = LRU_Cache(1)
test_cache.set(1, 5)
test_cache.set(None, 4)  # This should have no effect

assert test_cache.get(1) == 5  # Retrieving 1 should still be possible after previous step
assert test_cache.get(None) == -1  # Retrieving a value with key None should always return -1

# Test Case 3
print("3. Test DoublyLinkedList")
dll = DoublyLinkedList()
node1 = Node(1, 1)
node2 = Node(2, 2)

assert dll.is_empty()

dll.add_to_head(node1)

assert dll.head == node1
assert dll.tail == node1
assert dll.size == 1

dll.add_to_head(node2)

assert dll.head == node2
assert dll.tail == node1
assert dll.size == 2
assert dll.head.next == node1
assert dll.tail.prev == node2

dll.move_to_head(node1)

assert dll.head == node1
assert dll.tail == node2
assert dll.size == 2
assert dll.head.next == node2
assert dll.tail.prev == node1

dll.remove_tail()

assert dll.head == node1
assert dll.tail == node1
assert dll.size == 1
assert dll.head.next is None
assert dll.tail.prev is None

dll.remove_tail()

assert dll.head is None
assert dll.tail is None
assert dll.size == 0
assert dll.is_empty()
