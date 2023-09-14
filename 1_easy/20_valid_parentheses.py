class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)):
            return False
        return True

s = '()'
ob = Solution()

print(ob.isValid(s))