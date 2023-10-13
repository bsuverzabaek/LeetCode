# Sum of All Odd Length Subarrays
- Given an array of positive integers `arr`, return the sum of all possible odd-length subarrays of `arr`.
- A subarray is a contiguous subsequence of the array.

## Analysis
- Take 0,1,2,...,i elements on the left to get i+1 choices
- Take 0,1,2,...,n-1-i elements on the right to get n-i choices
- There are a total of k=(i+1)*(n-i) subarrays
- There are (k+1)/2 subarrays with odd length; there are k/2 subarrays with even length
