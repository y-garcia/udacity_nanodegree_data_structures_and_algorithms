# Explanation for Problem 3: Huffman Coding

# Overall approach
The `huffman_encoding` function is divided in 5 steps:
1. Iterate through the string of data and use a map to increase the frequency by 1
   for each character. A helper class `Node` is used to store the information.
2. Create a MinHeap to sort the Nodes by ascending frequency, such that popping from
   the Min Heap always return the smallest Node. 
3. Use the Min Heap to create a Huffman Tree as described in the exercise.
4. Traverse the Huffman tree to identify the coding for each character and store it
   in the Node object.
5. Iterate through the string of data and replace each character by its coding.

The `huffman_decoding` function iterates through the encoded string and navigates left
or right through the Huffman tree if it encounters a 0 or 1 in the encoded string. When
a leaf node containing a character is encountered, the character is added to the decoded
string and it jumps back up to the root of the Huffman tree to decode the next character.

# Time complexity
## `huffman_encoding`
In this case we assume the worst case: each character in the input string is unique.
1. Iterating through the string of data to count the frequency of its characters takes `O(n)`.
2. Creating a Min Heap consists of running the `heapify` function, which swaps each node with 
   its children if it's greater, starting from the root and down the height of the tree
   (`O(log n)`). This process is repeated for every element in the heap (`n`). So the overall
   complexity of this step is `O (n log n)`.
3. For the creation of the Huffmann tree, we iterate through all elements in the Min Heap,
   setting its left and right node in the process. This takes hence `O(n)`.
4. Traversing the complete Huffmann tree also takes `O(n)`, since each node is visited only once.
5. Iterating through the string of data to encode each character by its bit representation
   takes `O(n)`. 

# Space complexity
