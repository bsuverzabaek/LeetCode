class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        index = Counter(deck)
        indexValues = index.values()
        gcd = math.gcd(*indexValues)
        return gcd>=2
