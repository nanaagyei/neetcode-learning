class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowest = prices[0]

        for price in prices:
            if lowest > price:
                lowest = price
            maxProfit = max(maxProfit, price - lowest)
        
        return maxProfit