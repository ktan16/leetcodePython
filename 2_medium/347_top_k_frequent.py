class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # create dictionary to store key = num, val = occurrence
        counts = {}
        for i in range(len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1

        # sort dictionary by each item's value in descending order
        # {2: 7, 1: 6, 3: 8} -> {3: 8, 2: 7, 1: 6}
        counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        # return k_arr with top k elements
        k_arr = []
        for i in range(k):
            k_arr.append(counts[i][0])

        return k_arr
            

ob = Solution()

nums = [2,2,3,1,1,1]
k = 2

print(ob.topKFrequent(nums, k))