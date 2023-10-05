lass Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        comp = max(candies)
        for candy in candies:
            ans.append(candy+extraCandies>=comp)
        return ans
