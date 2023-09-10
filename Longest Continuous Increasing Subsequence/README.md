# Longest Continuous Increasing Subsequence
- Given an unsorted array of integers `nums`, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
- A continuous increasing subsequence is defined by two indices `l` and `r` (`l < r`) such that it is `[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]` and for each `l <= i < r`, `nums[i] < nums[i + 1]`.

## Analysis
- It would have made more sense to put `maxNum = max(maxNum,count)` in the first `if` statement rather than make the second `if` statement.
