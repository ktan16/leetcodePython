class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        matches = 0
        for i in nums:
            if i == 1:
                count += 1
                if count >= matches:
                    matches = count
            else:
                count = 0
            
        return matches

nums = [1,0,1,1,1,0,1]

ob = Solution()
print(ob.findMaxConsecutiveOnes(nums))