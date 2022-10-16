class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(nums)
        i = 1
        val = nums[0]

        while i < k:
            if nums[i] == val:
                del nums[i]
                i -= 1
                k -= 1
            else:
                val = nums[i]
            i += 1
        
        return k

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

ob = Solution()
k = ob.removeDuplicates(nums)
print(nums)
print(k)
