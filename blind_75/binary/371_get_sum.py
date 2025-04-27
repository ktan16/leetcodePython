class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        bitfix = 0xffffffff

        while (b & bitfix) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry

        return a & bitfix if b > 0 else a