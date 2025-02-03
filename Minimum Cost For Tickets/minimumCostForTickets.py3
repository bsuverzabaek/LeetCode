class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i == len(days):
                return 0

            if i in dp:
                return dp[i]

            dp[i] = float("inf")

            for dayPass, cost in zip([1, 7, 30], costs):
                j = i
                
                while j < len(days) and days[j] < days[i] + dayPass:
                    j += 1
                
                dp[i] = min(dp[i], cost + dfs(j))

            return dp[i]

        return dfs(0)
