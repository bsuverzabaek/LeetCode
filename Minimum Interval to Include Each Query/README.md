# Minimum Interval to Include Each Query

- You are given a 2D integer array `intervals`, where intervals[i] = [left<sub>i</sub>, right<sub>i</sub>] describes the i<sup>th</sup> interval starting at left<sub>i</sub> and ending at right<sub>i</sub> (inclusive). The size of an interval is defined as the number of integers it contains, or more formally right<sub>i</sub> - left<sub>i</sub> + 1.

- You are also given an integer array `queries`. The answer to the j<sup>th</sup> query is the size of the smallest interval `i` such that left<sub>i</sub> <= queries[j] <= right<sub>i</sub>. If no such interval exists, the answer is `-1`.

- Return an array containing the answers to the queries.

## Time Complexity
- O(NlogN + QlogQ)
