# LeetCode Problem: Two Sum
- Return indices of 2 numbers in an array such that that add up to an integer “target”

## Brute Force Method
- While the brute force method works fine, its complexity is O(N<sup>2</sup>)

## Optimized Method
- A hash map allows us to find the answer by iterating through the array only once
1. Initialize an empty `ans` array
2. Initialize an empty `index` hash
3. While iterating through the `nums` array:
  - Check if `target-nums[i]` is in `index`
    - If yes, append `index[target-nums[i]]` and `i` to `ans`
  - Assign `i` to `index[nums[i]]`
4. return `ans`

- Since a+b=target,
  - it follows that target-a=b and,
  - target-b=a
