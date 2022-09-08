class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # test
        for num in nums:
            if 0 in nums:
                index = nums.index(0)