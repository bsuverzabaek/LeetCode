# Number of Rectangles that Can Form the Largest Square
- You are given an array `rectangles` where `rectangles[i] = [li, wi]` represents the i<sup>th</sup> rectangle of length l<sub>i</sub> and width w<sub>i</sub>.
- You can cut the i<sup>th</sup> rectangle to form a square with a side length of `k` if both `k <= li` and `k <= wi`. For example, if you have a rectangle `[4,6]`, you can cut it to get a square with a side length of at most `4`.
- Let `maxLen` be the side length of the largest square you can obtain from any of the given rectangles.
- Return the number of rectangles that can make a square with a side length of `maxLen`.

## Analysis
- This is a good way to access individual elements in an array without making a nested `for` loop
