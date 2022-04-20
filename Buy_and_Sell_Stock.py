class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        start = 0
        end = 1
        max_profit=0

        for i in range(1,len(prices)):
            end = i
            profit = prices[end] - prices[start]
            if max_profit < profit:
                max_profit = profit
            if profit < 0:
                start = i
        return max_profit
                
