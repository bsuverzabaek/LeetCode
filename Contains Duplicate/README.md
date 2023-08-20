# Contains Duplicate
- Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

## Analysis
- I originally thought of using bitwise operators (in particualr with XOR), but I couldn't figure out a way to do so without making the time complexity N<sup>2</sup>
- Since sets can only have unique elements, it would get rid of duplicates once `nums` is implemented
- If the length of `nums` and its set are different, that must mean there was a duplicate
