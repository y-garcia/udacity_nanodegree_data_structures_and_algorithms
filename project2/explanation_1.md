# Explanation for Problem 1: LRU Cache

# Overall approach
In order to store and retrieve a value by its key in constant time, I have decided to use
a dictionary (hash map) as the internal data structure for the cache data.

Each entry in the dictionary can be retrieved by its key, and it contains yet another
dictionary with two pieces of information: the value stored under that key, plus the
order in which the value was used (that is, set or retrieved). See following example:

```
cache = {
#   'key': {'value': number, 'used_order': number},
    '100': {'value': 10, 'used_order': 2},
    '200': {'value': 20, 'used_order': 3},
    '300': {'value': 30, 'used_order': 1}
}
```

The usage order helps to decide which value was used the longest ago (key 300 above), in 
order to delete it when adding a new value when the cache has reached its maximum capacity.

# Detailed explanation
## get(key)
This method checks first whether the key exists. In that case, it increases its `used_order` 
and returns the value afterwards. If the key doesn't exist, or it is `None`, `-1` will be 
returned.

Checking key existence, storing the new `used_order` and retrieving its value are all 
operations that require constant time, so the overall **time complexity** is `O(1)` 

## set(key, value)
This method checks first whether the cache is at capacity. In that case
