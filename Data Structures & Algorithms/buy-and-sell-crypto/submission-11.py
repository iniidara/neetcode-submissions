class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Start with the first price as your minimum, and 0 profit
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            # 1. Update the lowest price seen so far
            if price < min_price:
                min_price = price
            # 2. Check if selling today beats your previous max profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
