# Best Poker Hand
- You are given an integer array `ranks` and a character array `suits`. You have `5` cards where the i<sup>th</sup> card has a rank of `ranks[i]` and a suit of `suits[i]`.
- The following are the types of poker hands you can make from best to worst:
1. `"Flush"`: Five cards of the same suit.
2. `"Three of a Kind"`: Three cards of the same rank.
3. `"Pair"`: Two cards of the same rank.
4. `"High Card"`: Any single card.
- Return a string representing the best type of poker hand you can make with the given cards.
- Note that the return values are case-sensitive.

## Analysis
- I don't actually have to use `Counter()` for `suits`; I could just use `set()` and determine its length
