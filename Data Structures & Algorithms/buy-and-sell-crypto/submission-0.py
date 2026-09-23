class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        minbuy = prices[0]
        max_profit = 0

        for price in prices:
            profit = price - minbuy
            max_profit = max(profit, max_profit)
            minbuy = min(minbuy, price)
        
        return max_profit