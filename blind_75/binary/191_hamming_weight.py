class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = 0

        while n:
            ones += n % 2 # will either be 1 or 0
            n = n >> 1 # bitshift integer to the right by 1 

        return ones
