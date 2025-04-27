class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp = max(nums)
        currMin, currMax = 1,1

        for num in nums:
            tmp = currMax * num # temp var to prevent min calc error
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(tmp, num * currMin, num)

            mp = max(mp, currMax)
        
        return mp

    def m_maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        
        mp = 0
        p = 1
        start = 0
        end = 0

        # sliding window technique
        # while start <= end and end < len(nums):
        while True:
            if end != len(nums) - 1:
                p *= nums[end]
            
            if p > mp:
                mp = p
                end += 1
            
            else:
                if end != len(nums) - 1:
                    end += 1
                else:
                    if nums[start] != 0:
                        p /= nums[start]
                    start += 1

            if start == end:
                break

        return mp

ob = Solution()

nums = [2,3,-2,4]
print(ob.maxProduct(nums))