# Original Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(len(prices)):
            if prices[i]-buy>profit:
                profit = prices[i]-buy
            if prices[i]<buy:
                buy = prices[i]
        return profit

# Better Solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
            profit = max(profit,prices[i]-buy)
            buy = min(buy,prices[i])
        return profit
