# Single Number
- Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.

## Analysis
- While the original solution fulfilled the O(N) constraint, it took up quite a bit of space
- I completely forgot about XOR
- If the inputs are different, XOR returns 1. If they are the same, it returns 0 because the same numbers return the same bits.
- The single element will always get returned because all the same numbers return 0. Also, 0^answer = answer.
