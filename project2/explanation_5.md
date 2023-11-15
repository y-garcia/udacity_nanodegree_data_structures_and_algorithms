# Explanation for Problem 5: Blockchain

# Overall approach
There are two main classes:
- Block
  - Block expects three arguments (`timestamp`, `data`, `previous_hash`) that cannot be `None`.
  - The method `calc_hash()` joins those attributes and calculates the hash.

- Blockchain
  - The Blockchain was implemented as a `LinkedList`. Each new block is inserted to the head
  and contains a reference to and the hash of the previous block (the next in the LinkedList). 
  - It has three methods:
    - `append()`: Adds a block to the head.
    - `length()`: Returns the number of blocks in the blockchain.
    - `is_valid()`: Checks whether the references and the hashes of all blocks are valid
  - No deletions or insertions are allowed, since blockchain transactions are supposed to be 
  irreversible and cannot be altered retroactively.

# Time complexity
- `Block.calch_hash()`: Contains only constant operations, so the time complexity is `O(1)`.
- `Blockchain.append()`: Adds a new block to the head and changes some references, so the time complexity is `O(1)`.
- `Blockchain.length()`: Returns a value, so the time complexity is `O(1)`.
- `Blockchain.is_valid()`: Iterates through the whole blockhain once, so the time complexity is `O(n)`.

# Space complexity
- `Block`: Data of constant size stored mainly in internal attributes, so the space complexity is `O(1)`.
- `Blockchain`: Keeps a reference to the head of the block, but each block is connected to each other,
so the whole Blockchain has a space complexity of `O(n)`.
