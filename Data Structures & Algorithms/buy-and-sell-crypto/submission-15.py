class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxPrice = 0

        for price in prices:
            if price < minprice:
                minprice = price
            elif price - minprice > maxPrice:
                maxPrice = price - minprice
                
        return maxPrice
                
        