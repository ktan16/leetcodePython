class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        matches = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                matches += 1
        return matches

nums = [5555,901,482,1771]

ob = Solution()
print(ob.findNumbers(nums))