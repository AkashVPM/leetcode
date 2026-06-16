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

      def maxProfit_2(self, prices: List[int]) -> int:
            l = 0
            profit = 0

            for i in range(len(prices)): 

                  if prices[l] > prices[i]: 
                        l = i
                        continue

                  a = prices[i] - prices[l]
                  profit = max(profit, a)
            
            return profit