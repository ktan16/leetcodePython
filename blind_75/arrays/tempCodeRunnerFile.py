class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] <= buy:
                buy = prices[i]
                buyindex = i

                for sellindex in range(buyindex, len(prices) - 1):
                    if prices[sellindex] - prices[buyindex] > profit:
                        profit = prices[sellindex] - prices[buyindex]
        
        return profit