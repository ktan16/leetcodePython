class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        poisoned = 0
        prev_time = 0

        for i in range(len(timeSeries) - 1):
            poisoned += min(timeSeries[i + 1] - timeSeries[i], duration)
        
        return poisoned + duration

ob = Solution()

timeSeries = [1, 4, 5]
duration = 2

print(ob.findPoisonedDuration(timeSeries, duration))