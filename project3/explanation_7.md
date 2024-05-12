# Explanation for Problem 7: Request Routing in a Web Server with a Trie

## Overall approach

There are 3 main classes:

- `RouterTrieNode`, which has
  - 2 properties: a `handler` and a dictionary of `children`. The `handler` is only set for leaf nodes.
  - 1 method: `insert(segment)`, which adds a new child to the `children` dictionary.

- `RouterTrie`, which has
  - 1 property: The `root` node, which is instantiated with the `root_handler`.
  - 2 methods:
    - `insert(segments, handler)`: Adds a node for every segment (text between two '/') of the path to the trie, setting
    the handler only for the leave node. Since this is a trie, all paths with the same prefix share the same segment 
    nodes.
    - `find(segments)`: Returns the node corresponding to the list of segments.

- `Router`, which has
  - 2 properties: The `routeTrie` above and a reference to a `not_found_handler`, for non-existing paths.
  - 3 methods:
    - `add_handler(path, handler)`: Calls `routeTrie.insert(path, handler)`.
    - `lookup(path)`: Calls `routeTrie.find(path)` or returns `not_found_handler` for non-existing paths.
    - `split_path(path)`: Splits a path by '/' into its segments.

## Time complexity

The only methods worth analyzing for time complexity are `RouterTrie.insert(segments, handler)` and 
`RouterTrie.find(segmets)`. The rest has $O(1)$ time complexity or calls one of those methods.

Both methods have a time complexity of $O(n)$, since they iterate through all segments in order to insert them into or
find them in the trie.

## Space complexity

As for space complexity, all methods just use some helper variables to iterate, so it's mostly $O(1)$.
For the RouterTrie as a whole it's $O(n)$ for $n$ segments, although in practice is less than that, since some paths
would share some of those nodes, which is the advantage of tries.