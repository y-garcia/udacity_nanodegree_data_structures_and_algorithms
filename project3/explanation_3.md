# Explanation for Problem 3: Rearrange Array Digits

## Overall approach

I use the merge sort algorithm to sort the array in **descending** order and then assign digits at even positions
to one number and the ones at odd positions to the second number, returning both numbers in an array as the result.

## Time complexity

Merge sort has a time complexity of `O(n log n)`, since it divides the array by half recursively `O(log n)` and
stitches those halves together in the right order in `O(n)`. For the seconds step of calculating the numbers with
maximum sum, I iterate through the sorted list assigning each alternating digit to one of the numbers. This takes 
`O(n)`.

So the total time complexity ist `O((n log n) + n)`, which can be simplified as `O(n log n)` as requested.

## Space complexity

Merge sort creates a **new** array in a sorted order, so its space complexity is linear `O(n)`. The result numbers are 
just 2 integers, regardless of the size of the input list, so its space complexity is constant `O(1)`, resulting in a
total space complexity of `O(n)`.