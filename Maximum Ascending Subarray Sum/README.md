# Maximum Ascending Subarray Sum
- Given an array of positive integers `nums`, return the maximum possible sum of an ascending subarray in `nums`.
- A subarray is defined as a contiguous sequence of numbers in an array.
- A subarray `[numsl, numsl+1, ..., numsr-1, numsr]` is ascending if for all `i` where `l <= i < r`, `nums[i]  < nums[i+1]`. Note that a subarray of size `1` is ascending.

## Analysis
- I think I could have shrunk it so that I didn't have to use the final `ans` logic
