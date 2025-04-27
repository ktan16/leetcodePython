class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                answer.append(nums[l] * nums[l])
                l += 1
            else:
                answer.append(nums[r] * nums[r])
                r -= 1

        return answer[::-1] #return reverse of array

nums = [-4, -1, 0, 3, 10]

ob = Solution()
print(ob.sortedSquares(nums))