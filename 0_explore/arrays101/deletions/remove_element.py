class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums)
        i = 0
        while i < k:
            if nums[i] == val:
                # del arr[0], pop()
                del nums[i]
                i -= 1
                k -= 1
            i += 1
        
        return k

nums = [3, 2, 2, 3]
val = 3

ob = Solution()
k = ob.removeElement(nums, val)
print(nums)
print(k)
