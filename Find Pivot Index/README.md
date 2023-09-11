# Find Pivot Index
- Given an array of integers `nums`, calculate the pivot index of this array.
- The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.
- If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.
- Return the leftmost pivot index. If no such index exists, return `-1`.

## Analysis
- Since I'm returning the first element of the `ans`, I should return the index as soon as `leftSum` and `rightSum` match, instead of storing it in a list
- Instead of the `i==0` block, I should just initialize `rightSum==0`. Then in the `for` loop, subtract `nums[i]` from `rightSum`. See if `leftSum` and `rightSum` match. Then, add `nums[i]` to `leftSum`
