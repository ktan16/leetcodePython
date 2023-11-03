class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Init results array to return
        results = []

        # Sort array to handle duplicates
        nums.sort()

        for i, num in enumerate(nums):
            # Ignore duplicates for first number
            if i > 0 and num == nums[i - 1]:
                continue
            
            # Two pointers at start and end of subarray next to i
            left = i + 1
            right = len(nums) - 1

            # While pointers do not intersect
            while left < right:
                # Temp sum
                sum = num + nums[left] + nums[right]

                if sum == 0:
                    # Triplet found, add to results
                    results.append([num, nums[left], nums[right]])

                    # Only have to update one pointer, other conditions will update pointers later on
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                # If total is greater than 0, move right pointer down to decrease sum
                elif sum > 0:
                    right -= 1
                
                # If total is less than 0, move left pointer up to increase sum
                else:
                    left += 1

        return results

ob = Solution()
nums = [-1,0,1,2,-1,-4]

print(ob.threeSum(nums))