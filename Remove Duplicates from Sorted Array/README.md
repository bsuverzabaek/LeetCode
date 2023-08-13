# Remove Duplicates from Sorted Array
- Return `k` unique elements from `nums`

## Solution
1. `k` starts as `1` since the first element is always unique
2. To compare the current element with the previous one, start the iteration from `1`:
  - If the current and previous elements are different, then the element is unique
    - If it is unique, `nums[k]` is updated with `nums[i]`. `k` is increased by `1` to mark the next index of the unique element
3. Return `k`

- Any duplicates are overwritten and `k` is the length of the new array

## Original Solution
- This solution does not work because `set` does not actually remove duplicates. It allocates extra space for another data structure (in this case, `set`), which is not allowed in the parameters
