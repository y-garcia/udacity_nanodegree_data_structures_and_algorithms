# Explanation for Problem 6: Union and Intersection

# Overall approach

I used the suggested implementation for `Node` and `LinkedList`. I then implemented following 3 functions:
- `union(linkedlist1, linkedlist2)`: This function just iterates through both LinkedLists and creates a new one with
  the same values as both.
- `union_distinct(linkedlist1, linkedlist2)`: Since it wasn't clear whether above function should remove duplicates
  or not, I implemented this function to do just that. It collects all **distinct** values from both LinkedLists and
  adds them to a new one.
- `intersection(linkedlist1, linkedlist2)`: This function finds the common values in both LinkedLists and adds them
  to a new one.

# Time complexity

In the following examples we assume both LinkedLists contain `n` nodes.

## union(linkedlist1, linkedlist2)

This function just iterates through every node of both LinkedLists and appends them to a new one. 

The given LinkedList implementation doesn't keep track of the tail, so we need to traverse to the
end of the LinkedList each time we want to append a new element, so appending to both lists takes:

`2 * ( O(1) + O(2) + ... + O(n-1) ) = 2 * O((n-1)n/2) = O(n^2)`

## union_distinct(linkedlist1, linkedlist2)

Since it wasn't clear whether above function should remove duplicates or not, I implemented this function to do 
just that. It collects all **distinct** values from both LinkedLists and adds them to a new one. 

This works similar to the function above, the only difference is that it keeps track of the elements that have been
already added to the LinkedLists in an internal set. Adding values to the internal set and checking if a value exists
in that settakes `O(1)` in Python, which is overriden by the `O(n^2)` it takes to append to both LinkedLists as
calculated above.

## intersection(linkedlist1, linkedlist2)

This function finds the common values in both LinkedLists and adds them to a new one.

It first iterates through the second LinkedList and adds all values to an internal set to keep track of common values.
It then iterates through the first LinkedList, and it also adds every value to an internal set to keep track of already
added values. At the same time it adds that value to the result LinkedList if it exists in the second LinkedList but
hasn't been already added.

Iterating through the second LinkedList and adding every value to an internal set takes `O(n)`.
Iterating through the first LinkedList and checking both internal sets for existence takes `O(n^2)` as calculated above.  

# Space complexity

In the following examples we also assume that both LinkedLists contain `n` nodes

## union(linkedlist1, linkedlist2)

We have two input LinkedLists, and we create a new one, so the space complexity is `O(3*n) = O(n)`.

## union_distinct(linkedlist1, linkedlist2)

Here we assume the worst case: all values are different in both lists.

Here we have two input LinkedLists, and we create a new one, as above.

In addition to that we keep track of common values in an internal, which can contain all the values of both lists,
so the overall space complexity is `O(5*n) = O(n)`.

## intersection(linkedlist1, linkedlist2)

**Case 1**: we assume all values are different in both lists and the intersection is empty.

We have two input LinkedLists, we add all values to internal sets, and the result LinkedList is empty, so the
space complexity is `O(4*n) = O(n)`.

**Case 2**: we assume both list contain the same values.

We have two input LinkedLists, we add all values to internal sets, and the result LinkedList contains also all
values, so the space complexity is `O(5*n) = O(n)`.

