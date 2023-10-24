# Kth Distinct String in an Array
- A distinct string is a string that is present only once in an array.
- Given an array of strings `arr`, and an integer `k`, return the k<sup>th</sup> distinct string present in `arr`. If there are fewer than `k` distinct strings, return an empty string `""`.
- Note that the strings are considered in the order in which they appear in the array.

## Analysis
- At first, I thought I could use `set()` to solve this, but `Counter()` turned out to be better
