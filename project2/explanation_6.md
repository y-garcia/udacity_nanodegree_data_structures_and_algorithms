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
- `union(linkedlist1, linkedlist2)`: This function just iterates through every node of both LinkedLists and appends
  them to a new one. The given LinkedList implementation doesn't keep track of the tail, so we need to traverse to the
  end of the LinkedList each time we want to append a new element, so appending to both lists takes 
  2 * ( O(1) + O(2) + ... + O(n-1) ) = 2 * O((n-1)n/2) = `O(n^2)`

- `union_distinct(linkedlist1, linkedlist2)`: Since it wasn't clear whether above function should remove duplicates
  or not, I implemented this function to do just that. It collects all **distinct** values from both LinkedLists and
  adds them to a new one.

- `intersection(linkedlist1, linkedlist2)`: This function finds the common values in both LinkedLists and adds them
  to a new one.

# Space complexity
