class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums) - 1):
            for k in range(i + 1, len(nums)):
                if nums[i] + nums[k] == target:
                    return([i, k])

        return []

nums = [2,7,11,15]
target = 9

ob1 = Solution()
print(ob1.twoSum(nums, target))
