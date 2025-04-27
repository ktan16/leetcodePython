class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n + 1)

        for i in range(n + 1):
            bin_str = str(bin(i))[2:]

            ones = 0
            for n in bin_str:
                ones += int(n)
                
            ans[i] = ones

        return ans
    
n = 2

ob = Solution()
print(ob.countBits(n))