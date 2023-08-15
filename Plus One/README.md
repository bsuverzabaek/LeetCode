# Plus One

- You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the i<sup>th</sup> digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's. Increment the large integer by one and return the resulting array of digits.

## Solution
- Start from the end of `digits`:
  - If `digits[i]` is `9`, change it to `0`
  - Else, add `1` to `digits[i]` then return it
- Add `digits` to `[1]` to get `1` as the starting element, then return it

## Analysis
- Although my original solution was accepted, it required 2 `for` loops, which effected its performance.
- The better solution only needed 1 `for` loop.
- I didn't know that `[1]+digits` could be done
- Starting from the rear made more sense than starting from the head
