class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            
            potential = w * h
            maxArea = max(maxArea, potential)
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxArea

height = [1,8,6,2,5,4,8,3,7]

ob = Solution()
print(ob.maxArea(height))