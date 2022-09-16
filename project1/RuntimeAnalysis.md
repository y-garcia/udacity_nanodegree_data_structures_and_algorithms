# Task 0

Setting variables and accessing elements in a list have constant time complexity in python.
Since this is all we do in this task the time complexity of Task 0 is `O(1)`.

# Task 1

In this task we iterate through all elements of the texts and calls files and then
do constant operations inside it, like accessing an element and adding it to a set.

So the time complexity of Task 1 is `O(n+m)` where

    `n` = number of records in the texts file
    `m` = number of records in the calls file

# Task 2

In this task we iterate through all calls. Inside the loop we do constant operations
like accessing elements in a list, checking if a dictionary key exists, adding keys
to a dictionary and adding a number to its value. So the time complexity for the
loop is `O(n)`, where `n` is number of records in the calls file.

After that we search for the maximum duration, which has the time complexity `O(2n)` in
the worst case where every incoming and answering number in the calls file is unique.

After that we search for the index of the maximum duration using `duration.index()`
which also has a time complexity of `O(2n)`

Hence, all operations in this task are linear, so we could approximate the time
complexity of Task 2 as being `O(n)`.

# Task 3

Here we have two methods:
 1. `get_area_codes_from_bangalore(calls_list)`
    
    In this first method we iterate through all calls, set a couple of variables,
    access a couple of elements from the calls list, and check whether the numbers
    have a specific pattern using regular expressions. The regular expressions
    may be inefficient in some cases, but due to nearly constant length of the 
    numbers and the expressions themselves, we can assume constant time for the
    regular expressions and should be negligible in comparison to the size of 
    the calls list. So we can approximate the loop as having time complexity `O(n)`.

    After that, we sort the list, which takes `O(n log n)` in the worst case using
    **timsort**.

    The worst-case time complexity of this method is hence `O(n log n)`, since
    `O(n log n)` behaves worse than `O(n)` for large values. 

 2. `get_local_calls_from_bangalore(calls_list)`

    In this second method we iterate through the calls list. Inside the loop we set some
    variables, check some conditions and increase some variables by one, all of which have
    a constant time complexity. Afterwards we make a simple mathematical operation. Hence,
    the time complexity of this method is `O(n)`, since it depends primarily on the size
    of the calls list.

# Task 4

In this task we make two iterations. Inside both loops we compute simple constant operations
so their effect on the overall time complexity can be neglected. The first loop iterates as 
many times as the maximum number of items of either the texts list or the calls list, whichever
is longer. The second loop iterates through the calls list. Assuming the calls list is 
longer and contains n items, both this loops would take `O(n)` to complete.

After that, we sort the list of telemarketers, which has been filled throughout above loops.
Assuming the worst case that all outgoing numbers are telemarketers, the sorting would take
`O(n log n)` using **timsort**.

The worst-case time complexity of this method is hence `O(n log n)`, since
`O(n log n)` behaves worse than `O(n)` for large values. 