# Find Subarrays With Equal Sum
- Given a 0-indexed integer array `nums`, determine whether there exist two subarrays of length `2` with equal sum. Note that the two subarrays must begin at different indices.
- Return `true` if these subarrays exist, and `false` otherwise.
- A subarray is a contiguous non-empty sequence of elements within an array.

## Analysis
- `pairwise()` is a useful way to get successive overlapping pairs
- pairwise(ABCDEFG) -> AB BC CD DE EF FG
- `:=` is the walrus operator that works as an assignment operator
- n=30; if n>10: ... == if (n:=30)>10: ...
