class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        combined = ""
        result = []

        for digit in digits:
            combined += str(digit)

        combined = int(combined) + 1

        for c in str(combined):
            result.append(int(c))

        return result   

ob = Solution()

digits = [1,2,3]

print(ob.plusOne(digits))