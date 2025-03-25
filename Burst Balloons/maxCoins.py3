class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in range(len(nums))]

        for left in range(len(nums) - 2, 0, -1):
            for right in range(left, len(nums) - 1):
                for i in range(left, right + 1):
                    coins = nums[left - 1] * nums[i] * nums[right + 1]
                    coins += dp[left][i - 1] + dp[i + 1][right]
                    dp[left][right] = max(dp[left][right], coins)

        return dp[1][len(nums) - 2]
