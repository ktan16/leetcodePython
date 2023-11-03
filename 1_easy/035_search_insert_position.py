class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[len(nums) - 1] < target:
            return len(nums)
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

            

ob = Solution()

nums = [1,3,5,6]
target = 7

print(ob.searchInsert(nums, target))