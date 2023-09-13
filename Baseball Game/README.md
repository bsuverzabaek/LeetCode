# Baseball Game
- You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.
- You are given a list of strings `operations`, where `operations[i]` is the i<sup>th</sup> operation you must apply to the record and is one of the following:
- An integer `x`.
  - Record a new score of `x`.
- `'+'`.
  - Record a new score that is the sum of the previous two scores.
- `'D'`.
  - Record a new score that is the double of the previous score.
- `'C'`.
  - Invalidate the previous score, removing it from the record.
- Return the sum of all the scores on the record after applying all the operations.

## Analysis
- This was one of the easier problems
