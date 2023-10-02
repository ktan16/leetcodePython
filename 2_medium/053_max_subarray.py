class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # max result start at first num in arr
        # initialize current sum as 0
        result = nums[0]
        currsum = 0

        for num in nums:
            # if previously calculated sum is < 0, restart cursum
            if currsum < 0:
                currsum = 0

            # align currsum with currnum
            currsum += num

            # result is max between previous result and current sum
            result = max(result, currsum)
        
        return result

        
ob = Solution()

nums = [5,4,-1,7,8]

print(ob.maxSubArray(nums))