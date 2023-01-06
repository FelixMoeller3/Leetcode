from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curBuy= prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] < curBuy:
                curBuy = prices[i]
            elif prices[i]-curBuy > profit:
                profit = prices[i] - curBuy
            
        return profit