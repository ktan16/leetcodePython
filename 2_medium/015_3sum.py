class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s_arr = sorted(nums)
        result = []
        print(s_arr)
        for i in range(len(s_arr) - 2):
            left = i + 1
            right = len(s_arr) - 1

        return result

ob = Solution()
nums = [-1,0,1,2,-1,-4]

print(ob.threeSum(nums))