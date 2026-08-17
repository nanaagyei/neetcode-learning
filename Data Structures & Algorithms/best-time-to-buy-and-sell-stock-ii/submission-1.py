class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_price = prices[0]

        for i in range(1, len(prices)):
            if current_price < prices[i]:
                max_profit += (prices[i] - current_price)
            current_price = prices[i]
        
        return max_profit