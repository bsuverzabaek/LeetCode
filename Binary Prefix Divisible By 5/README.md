# Binary Prefix Divisible By 5
- You are given a binary array `nums` (0-indexed).
- We define x<sub>i</sub> as the number whose binary representation is the subarray `nums[0..i]` (from most-significant-bit to least-significant-bit).
  - For example, if `nums = [1,0,1]`, then `x0 = 1`, `x1 = 2`, and `x2 = 5`.
- Return an array of booleans `answer` where `answer[i]` is `true` if x<sub>i</sub> is divisible by `5`.

## Analysis
- I really should take more time to think about initializing `val` instead of over-complicating it
