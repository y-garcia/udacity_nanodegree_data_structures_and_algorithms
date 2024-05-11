# Explanation for Problem 6: Unsorted Integer Array

## Overall approach

I iterate once through the list, keeping track of the minimum and maximum number I've encountered so far, updating them
with a new value if I encounter one that is smaller than the minimum or greater than the maximum.

## Time complexity

$O(n)$, since I traverse the list once.

## Space complexity

$O(1)$, since I just use 2 variables for keeping track of the minimum and maximum value, regardless of
the size of the input list.