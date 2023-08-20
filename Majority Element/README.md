# Majority Element
- Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

## Analysis
- The Boyer-Moore Majority Voting Algorithm is used to find the majority element that has more than `N/2` occurrences.
- I had no idea about this algorithm; I initially thought about using bitwise operators
- This algorithm establishes that the majority element will always be in the lead, even after encountering other elements
- This algorithm assumes the majority element occurs more than `N/2` times
  - This assumption guarantees that even if `count` goes back to `0`, the majority element will retake the lead
