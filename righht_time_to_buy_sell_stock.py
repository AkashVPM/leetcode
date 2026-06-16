class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        profit = 0

        for i in range(len(prices)): 
            a = prices[l] - prices[i]
            
            if a > 0: 
                l = i
            if a < 0: 
                profit = max(profit, abs(a))
        
        return profit