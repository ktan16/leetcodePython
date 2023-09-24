class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        longest = 0

        for num in nums:
            # if num - 1 not in set, then num is start of sequence
            if (num - 1) not in set_nums:
                length = 0
                # keep finding num + 1 until doesn't exist
                while (num + length) in set_nums:
                    length += 1
                # get longest using max
                longest = max(length, longest)
            
        return longest

ob = Solution()
nums = [100, 4, 200, 1, 3, 2]

print(ob.longestConsecutive(nums))