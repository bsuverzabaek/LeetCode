# Longest Harmonious Subsequence
- We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly `1`.
- Given an integer array `nums`, return the length of its longest harmonious subsequence among all its possible subsequences.
- A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

## Analysis
- I should have iterated through the dict instead of the list itself
- Iterating through the list led to a bad run time
- My way led to a lot of redundancies that I didn't know how to reduce
