class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums and i != nums.index(x):
                i1 = nums.index(x)
                return [i, i1]

nums = [3, 3]
target = 6

ob = Solution()
print(ob.twoSum(nums, target))

