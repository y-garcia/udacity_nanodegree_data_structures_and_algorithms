class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Capacity must be a positive number
        if capacity is None or capacity <= 0:
            raise ValueError("Capacity must be an integer greater than 0")

        # Initialize class variables
        self.cache = {}
        self.capacity = capacity
        self.used_order = -1

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache:
            self.used_order += 1
            self.cache[key]['used_order'] = self.used_order
            return self.cache[key]['value']

        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key is None:
            return

        if len(self.cache) == self.capacity:
            oldest_key = self.get_oldest_key()
            self.delete(oldest_key)

        if key not in self.cache:
            self.used_order += 1
            self.cache[key] = {'value': value, 'used_order': self.used_order}

    def delete(self, key):
        if key is None:
            return

        if key in self.cache:
            del self.cache[key]

    def get_oldest_key(self):
        oldest_key = -1
        for key in self.cache:
            if oldest_key == -1 or self.cache[key]['used_order'] < self.cache[oldest_key]['used_order']:
                oldest_key = key

        return oldest_key

    def __str__(self):
        return str(self.cache)


our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


assert our_cache.get(1) == 1      # returns 1
assert our_cache.get(2) == 2      # returns 2
assert our_cache.get(9) == -1     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

assert our_cache.get(3) == -1      # returns -1 because the cache reached its capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
# Cache must be instantiated with a capacity greater than 0
try:
    LRU_Cache(None)  # This should raise a ValueError exception
except ValueError as e:
    assert str(e) == "Capacity must be an integer greater than 0"

try:
    LRU_Cache(-1)  # This should raise a ValueError exception
except ValueError as e:
    assert str(e) == "Capacity must be an integer greater than 0"

# Test Case 2
# Setting an empty key should have no effect and no old values should be deleted at capacity in that case
test_cache = LRU_Cache(1)
test_cache.set(1, 5)
test_cache.set(None, 4)  # This should have no effect

assert test_cache.get(1) == 5      # Retrieving 1 should still be possible after previous step
assert test_cache.get(None) == -1  # Retrieving a value with key None should always return -1

# Test Case 3
# Test the helper method "delete(key)"
test_cache = LRU_Cache(2)
test_cache.set(1, 1)
test_cache.set(2, 2)  # cache is now at capacity and key 1 is the oldest

test_cache.delete(2)
assert test_cache.get(2) == -1  # key 2 should not exist after previous step

test_cache.set(3, 3)  # adding a new value should not delete the oldest key 1 yet
assert test_cache.get(1) == 1
assert test_cache.get(3) == 3

# Test Case 4
# Test the helper method "get_oldest_key()"
test_cache = LRU_Cache(2)
test_cache.set(1, 1)
test_cache.set(2, 2)  # cache is now at capacity and key 1 is the oldest
assert test_cache.get_oldest_key() == 1
test_cache.get(1)     # cache is still at capacity and key 2 is the oldest
assert test_cache.get_oldest_key() == 2

