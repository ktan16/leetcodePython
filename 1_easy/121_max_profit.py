class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Sliding Window
        
        l, r = 0, 1 # two pointers for buy and sell indices
        profit = 0

        while r < len(prices):

            if prices[l] < prices[r]: # if buy day < sell day
                potential = prices[r] - prices[l] # calculate profit
                profit = max(profit, potential) # choose biggest

            else:
                l = r # if buy > sell, set buy day to that sell day
            r += 1 # increment sell day

        return profit
        
prices = [7, 1, 5, 3, 6, 4]
ob = Solution()

print(ob.maxProfit(prices))