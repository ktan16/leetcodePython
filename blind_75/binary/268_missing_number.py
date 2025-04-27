class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n not in nums:
            return n
        
        for i in range(n):
            if i not in nums:
                return i

nums = [0,1]

ob = Solution()
print(ob.missingNumber(nums))