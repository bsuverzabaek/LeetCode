# Minimum Cost to Move Chips to The Same Position
- We have `n` chips, where the position of the i<sup>th</sup> chip is `position[i]`.
- We need to move all the chips to the same position. In one step, we can change the position of the i<sup>th</sup> chip from `position[i]` to:
  - `position[i] + 2` or `position[i] - 2` with `cost = 0`.
  - `position[i] + 1` or `position[i] - 1` with `cost = 1`.
- Return the minimum cost needed to move all the chips to the same position.

## Analysis
- One of the examples given was quite confusing, so it messed with my understanding of this question
