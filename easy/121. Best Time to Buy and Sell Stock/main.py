from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[buy]:
                buy = i
            else:
                profit = max(profit, prices[i] - prices[buy])

        return profit
        

prices = [7,2,1,3,6,4]

s = Solution()

print(s.maxProfit(prices))
