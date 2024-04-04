# Explanation for Problem 2: Search in a Rotated Sorted Array

## Overall approach
I use the binary search concept twice. A modified version to search for the pivot at which the the array was rotated
and a second one to run a proper binary search on the right half of the array.

## Time complexity
Two binary searches after each other would have a time complexity of `O(2 log n)`, which can be generalized to
`O(log n)`.

## Space complexity
Since we just pass the indices of the subarray we are searching in on each iteration and don't create or slice new 
arrays, we just need space for storing a couple of internal variables, hence the space complexity is `O(1)`.