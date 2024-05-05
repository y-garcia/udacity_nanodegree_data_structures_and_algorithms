# Explanation for Problem 1: Square Root of an Integer

## Overall approach

The same idea as for a binary search is used:
1. I square the number at the midpoint and check if it corresponds to our target.
2. If it's smaller, I repeat on the lower half
3. If it's greater, I repeat on the upper half

## Time complexity

`O(log n)`, since we split the number's space in half on each iteration.

## Space complexity

`O(1)`, since no additional space that scales with the input size is needed.