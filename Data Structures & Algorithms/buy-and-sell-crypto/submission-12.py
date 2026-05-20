class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP solution
        maxProfit = 0
        minBuy = prices[0]

        for sell in prices:
            maxProfit = max(maxProfit, sell - minBuy)
            minBuy = min(minBuy, sell)

        return maxProfit