class Solution(object): # easy
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
            
    def s_twoSum(self, nums, target):
        dic = {} # key = nums[i], val = i
        for i in range(len(nums)):
            x = target - nums[i] # x = difference
            if x in dic: # if difference is found in dic
                return [dic[x], i] # return index of difference and current index
            else:
                dic[x] = i # else add new entry to dic
        return

nums = [3, 3]
target = 6

ob = Solution()
print(ob.s_twoSum(nums, target))

