# Find All K-Distant Indices in an Array
- You are given a 0-indexed integer array `nums` and two integers `key` and `k`. A k-distant index is an index `i` of `nums` for which there exists at least one index `j` such that `|i - j| <= k` and `nums[j] == key`.
- Return a list of all k-distant indices sorted in increasing order.

## Analysis
- My original idea was to make two passes through `nums`, but this made more sense in that I only pass through it once and do both neccessary functions at the same time
