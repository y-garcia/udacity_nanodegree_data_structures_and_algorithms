# Explanation for Problem 4: Active Directory

## Overall approach

I use a recursive function to walk through all groups in search of the desired username.
First I check if the user is in the current group, by looking for the name in the `users` list.
If not, I iterate through all subgroups and run the same function recursively for each group,
returning `True` if it is found in any of the subgroups. Otherwise, `False` is returned.

## Time complexity

- Let `T(n)` be the time it takes to run `is_user_in_group(user, group)` for a particular group.
- Let `g` be the number of subgroups in that group. 
- Let `u` be the number of users in that group.
- For simplicity reasons, let's assume that all groups contain the same number of
subgroups and users. 
- Let the last directory contain only `u` users and no subgroups.

In that case, the time complexity for each recursion would be:

```
T(n) = g * T(n-1) + u
T(n-1) = g * T(n-2) + u
.
.
.
T(1) = g * T(0) + u
T(0) = u
```

For 3 levels this would mean:

`T(3) = g * (g * (g * (u) + u) + u) + u = g^3u + g^2u + gu + u`

So for `n` levels we would have:

`T(n) = ug^n + ug^(n-1) + ... + ug^2 + ug + u`

So the overall time complexity would be `O(g^n)`.

## Space complexity

We really only store the return value whilst walking through the different groups. So we can assume
`O(1)` for each recursion.
- Let `T(n)` be the space needed for `is_user_in_group(user, group)` for a particular group.
- Let `c` be a constant representing the space complexity for each recursion. 

```
T(n) = c * T(n-1)
T(n-1) = c * T(n-2)
.
.
.
T(1) = c * T(0)
T(0) = c
```

So the overall space complexity would be: `O(c^n)`