# Search Insert Position
- Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
  - You must write an algorithm with O(log n) runtime complexity.
 
## Solution
- Initialize `ans` as `None`
- If `target` is equal to or less than the first element:
  - Set `ans` to `0`
- If not:
  - Iterating through `nums` starting from index `1`:
    - If `nums[i]` is equal to `target`:
      - Set `ans` to `i`, then break
    - If `target` is greater than `nums[i-1]` and less than `nums[i]`:
      - Set `ans` to `i`, then break
- If `ans` is still `None` (meaning `target` is the largest element):
  - Set `ans` to the length of `nums`
- Return `ans`

## Analysis
- I'm not too sure if this is O(log n) (probably not, since there is a for loop), but it was accepted with the runtime and memory beating 88.42% and 86.88% of Python3 users, respectively.
