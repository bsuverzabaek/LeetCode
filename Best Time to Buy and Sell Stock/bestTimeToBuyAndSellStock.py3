class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) == 0:
            return 0

        minPrice, profit = prices[0], 0

        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]

            if prices[i] - minPrice > profit:
                profit = prices[i] - minPrice

        return profit
