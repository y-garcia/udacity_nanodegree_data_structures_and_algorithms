# Explanation for Problem 5: Autocomplete with Tries

## Overall approach

Parting from a node I iterate through all its children, concatenating the parent suffix with each child's character on
each recursion, and adding complete suffixes to the `result` parameter if I encounter the end of a word.

## Time complexity

- Let $T(n)$ be the time it takes to run `suffixes(suffix, result)` for a particular node.
- Let $k$ be the number of children of that node.
- For simplicity reasons, let's assume that all nodes contain the same number of children. 
- Let the last node contain no children.

In that case, the time complexity for each recursion would be:

$$
T(n) = k T(n-1) + c
T(n-1) = k T(n-2) + c
.
.
.
T(1) = k T(0) + c
T(0) = c
$$

For 3 levels this would mean:

$T(3) = k * (k * (k * (c) + c) + c) + c = ck^3 + ck^2 + ck + c$

So for $n$ levels we would have:

$T(n) = ck^n + ck^(n-1) + ... + ck^2 + ck + c$

So the overall **time complexity** would be $O(k^n)$.

## Space complexity

The worst case space complexity can be boiled down to the size of the `result` list if we part from the root node, which
corresponds to the number of words in the trie, or the number of nodes with `is_word = True`. So, if the trie has $n$ 
nodes, the space complexity would be normally less than that, so the worst case **space complexity** is $O(n)$.