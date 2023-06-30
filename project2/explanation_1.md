# Explanation for Problem 1: LRU Cache

# Overall approach
In order to store and retrieve a value by its key in constant time, I have decided to use
a **dictionary** (hash map) as the internal data structure for the **cache** data.

To keep track of the order in which the elements have been used, I am using a **queue**
implemented as a **DoublyLinkedList**. This allows me to add recently used elements at the
beginning and removing the least used element at the end of the queue in constant time.

To avoid iterating through the DoublyLinkedList to move an element to the head after being 
used, I add a reference to the node to the cache under its key. So retrieving a Node in
the DoublyLinkedList, as well as inserting it to its head, is a constant time operation.

## Space complexity
If we define `n` as all possible (key, value) pairs that can be added to the cache, we see
that the cache (hash map) as well as the queue (DoublyLinkedList) are always at most as
long as the cache capacity, meaning that its independent of `n`.

So the overall **space complexity** is `O(1)`.

# Detailed explanation
## LRU_Cache.get(key)
This method checks first whether the key exists. In that case, it moves the corresponding
node in the queue to the head, as it is now the most recently used key. Afterwards the value
is returned. If the key doesn't exist, `-1` will be returned.

### Time complexity
Checking key existence, moving the node to the head and returning its value are all 
operations that require constant time, so the overall **time complexity** is `O(1)` 

## LRU_Cache.set(key, value)
After checking that the key is not `None` and it exists, this method checks whether the cache 
is at capacity. In that case the method `remove_oldest()` is called, which removes the tail
from the queue and removes the key and its content from the cache.

Afterwards a new node is added to the head of the queue, as it is now the most recently used
key and added to the cache under its key.

### Time complexity
Checking key existence, removing the last element in the queue, and adding a new element to
the head of the queue and to the cache are all operations that require constant time, since
no iteration is required.

So the overall **time complexity** is `O(1)`.
