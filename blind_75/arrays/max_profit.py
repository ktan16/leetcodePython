class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # set cheapest and profit
        cheapest = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < cheapest: # is current price the cheapest one we found
                cheapest = prices[i]
            
            if prices[i] - cheapest > profit: # if i subtract current price and cheapest price, is my profit greater
                profit = prices[i] - cheapest # if so update profit
            
        return profit

prices = [7, 1, 5, 3, 6, 4]
prices2 = [1,2]
ob = Solution()

print(ob.maxProfit(prices))