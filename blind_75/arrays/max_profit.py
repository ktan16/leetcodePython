class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        for i in range(1, len(prices) - 1):
            if prices[i] < buy:
                buy = prices[i]
                buyindex = i
        
        