# Merge Similar Items
- You are given two 2D integer arrays, `items1` and `items2`, representing two sets of items. Each array `items` has the following properties:
  - `items[i] = [valuei, weighti]` where value<sub>i</sub> represents the value and weight<sub>i</sub> represents the weight of the i<sup>th</sup> item.
  - The value of each item in `items` is unique.
- Return a 2D integer array `ret` where `ret[i] = [valuei, weighti]`, with weight<sub>i</sub> being the sum of weights of all items with value value<sub>i</sub>.
- Note: `ret` should be returned in ascending order by value.

## Analysis
- I didn't know you could use `Counter()` for arrays
