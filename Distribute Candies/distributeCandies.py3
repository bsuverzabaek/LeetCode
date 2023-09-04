class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        a = len(candyType)//2
        b = len(set(candyType))
        return a if a<=b else b
