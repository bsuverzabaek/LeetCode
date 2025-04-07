class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        ans = 0

        while left <= right:
            mid = left + ((right - left) // 2)
            coins = (mid / 2) * (mid + 1)

            if coins > n:
                right = mid - 1
            else:
                left = mid + 1
                ans = max(ans, mid)

        return ans
