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

In that case the time complexity for each recursion would be:

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
TODO