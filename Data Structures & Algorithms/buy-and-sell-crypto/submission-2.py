class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = prices[0]
        high = prices[0]

        profit = 0

        for n in prices:
            
            if n < low:
                low = n
                high = 0
            
            high = max(high, n)

            profit = max(profit, (high - low))

        return profit