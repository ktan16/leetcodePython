class Solution(object): # easy
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        myset = set(nums) # convert to set; does not contain dups
        if len(myset) == len(nums): # if len set == len list, no dups
            return False
        return True

nums = [1,2,3,1]

ob = Solution()
print(ob.containsDuplicate(nums))