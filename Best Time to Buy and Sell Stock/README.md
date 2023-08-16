# Best Time to Buy and Sell Stock
- You are given an array prices where `prices[i]` is the price of a given stock on the i<sup>th</sup> day.
- You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
- Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

## Solution
- Initialize `profit` as `0`
- Initialize `buy` as the first element
- Iterate through `prices` starting from the 2nd element:
  - Set `profit` as the max between `profit` and `prices[i]-buy`
  - Set `buy` as the min between `buy` and `prices[i]`
- Return `profit`

## Analysis
- The logic between the original and better solutions are the same, just some of the syntax is different
- The runtime of the original solution beat 94.81% but the memory only beat 19.72%
- The runtime of the better solution beat 72.64% and the memory beat 92.76%
- Changing the syntax can lead to better performance in some areas
