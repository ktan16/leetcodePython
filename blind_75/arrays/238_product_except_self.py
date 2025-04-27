class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        # create answer, left product, and right product array
        answer = [1] * n
        lp_arr = [1] * n
        rp_arr = [1] * n

        # calculate product to the left of each nums[i]
        # lp_arr[i] = product of all things left of it
        # first item is default to 1
        # [1,2,3,4] => [1,1,2,6]
        lp = 1
        for i in range(n):
            lp_arr[i] = lp
            lp *= nums[i]
        
        # calculate product to the right of each nums[i]
        # rp_arr[i] = product of all things right of it
        # last item is default to 1
        # [1,2,3,4] => [24,12,4,1]
        rp = 1
        for i in range(n - 1, -1, -1):
            rp_arr[i] = rp
            rp *= nums[i]
        
        # multiply lp_arr[i] to each rp_arr[i] for answer
        for i in range(n):
            answer[i] = lp_arr[i] * rp_arr[i]
            
        return answer
    
    def s_productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer

nums = [1,2,3,4]

ob = Solution()
print(ob.productExceptSelf(nums))