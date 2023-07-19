# Explanation for Problem 2: File Recursion

# Overall approach
To walk through all files in the given directory, I start at the root and list all files and
folders contained in it. Then I iterate through them: if I encounter a file with the ".c" 
extension, I add it to a python list. If I encounter a folder, I call the function recursively
on that folder, adding its return value to above list. At the end, the list is returned.

# Time complexity
- Let `T(n)` be the time it takes to run `find_files(suffix, path)` for a particular path.
- Let `d` be the number of directories in that path. 
- Let `k` be the number of files in that path.
- For simplicity reasons, let's assume that all directories contain the same number of
directories and files. 
- Let the last directory contain only `k` files and no directories.

In that case, the time complexity for each recursion would be:

```
T(n) = d * T(n-1) + k
T(n-1) = d * T(n-2) + k
.
.
.
T(1) = d * T(0) + k
T(0) = k
```
For 3 levels this would mean:

`T(3) = d * (d * (d * (k) + k) + k) + k = d^3k + d^2k + dk + k`

So for `n` levels we would have:

`T(n) = kd^n + kd^(n-1) + ... + kd^2 + kd + k`

So the overall time complexity would be `O(d^n)`.

# Space complexity
For each recursion two lists are used:
1. The `items` list, where we store all files and directories in the current path.
2. The `c_files` list, where we store all files with the ".c" extension.

Using the same definition as in the Time complexity section above, and assuming the worst
case scenario in which all files have a ".c" extension:
1. The `items` list would have a space complexity of `d + k` for each recursion
2. The `c_files` list would have a space complexity of `k` for each recursion

In the last recursion we only have files with ".c" extension and, thus, a space complexity
of `k + k`.

The space complexity for each recursion would then be:
```
T(n) = (d + k) + k + d * T(n-1) = d + 2k + d * T(n-1)
T(n-1) = d + 2k + d * T(n-2)
.
.
.
T(1) = d + 2k + d * T(0)
T(0) = k + k
```
For 3 levels this would mean:

```
T(3) = d + 2k + d * (d + 2k + d * (d + 2k + d * (2k)))
     = d + 2k + d^2 + 2kd + d^3 + 2kd^2 + 2kd^3
     = (2k+1)d^3 + (2k+1)d^2 + (2k+1)d + 2k
     = (2k+1)(d^3 + d^2 + d) + 2k
```

So for `n` levels we would have:

`T(n) = (2k+1)(d^n + d^(n-1) + ... + d^1) + 2k`

So the overall space complexity would be `O(d^n)`.
