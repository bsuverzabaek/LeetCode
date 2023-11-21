class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        rankIndex = Counter(ranks)
        suitIndex = Counter(suits)
        if max(suitIndex.values())==5:
            return "Flush"
        maxRank = max(rankIndex.values())
        if maxRank>=3:
            return "Three of a Kind"
        if maxRank>=2:
            return "Pair"
        return "High Card"
