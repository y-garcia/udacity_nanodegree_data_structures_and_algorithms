# Explanation for Problem 4: Dutch National Flag Problem

## Overall approach

I keep track of two pointers: the next position for a 0 and for a 2. Then I iterate through the list moving 0's to the
front and 2's to the back of the list, updating the corresponding indexes as I go. The 1's get sorted automagically ;-).

## Time complexity

Since the list gets sorted in one pass, the algorithm has a time complexity of `O(n)`.

## Space complexity

The space complexity is `O(1)`, since the list gets sorted in place.