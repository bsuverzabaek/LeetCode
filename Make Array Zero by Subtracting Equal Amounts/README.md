# Make Array Zero by Subtracting Equal Amounts
- You are given a non-negative integer array `nums`. In one operation, you must:
  - Choose a positive integer `x` such that `x` is less than or equal to the smallest non-zero element in `nums`.
  - Subtract `x` from every positive element in `nums`.
- Return the minimum number of operations to make every element in `nums` equal to `0`.

## Analysis
- Instead of using the brute force method, you can just count the number of unique elements and remove the `0` since it won't be necessary
