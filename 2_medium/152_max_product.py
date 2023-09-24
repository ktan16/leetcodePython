class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp = 0
        start = 0
        end = 0
        p = nums[end]

        while end < len(nums):
            
            if p >= mp:
                mp = p
                end += 1
                p *= nums[end]
            elif p < mp and end - start > 1:
                p /= nums[start]
                start += 1
            elif p < mp and end - start == 1:
                end += 1
                p *= nums[end]
                
        return mp

ob = Solution()

nums = [2,3,-2,4]
print(ob.maxProduct(nums))