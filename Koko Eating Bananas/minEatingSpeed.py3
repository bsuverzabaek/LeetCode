class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            k = left + ((right - left) // 2)
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/k)

            if hours <= h:
                ans = k
                right = k - 1
            else:
                left = k + 1

        return ans
