class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ROMAN = {
            "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000
        }

        num = 0
        i = 0

        while i < len(s) - 1:
            if ROMAN[s[i + 1]] > ROMAN[s[i]]:
                num += ROMAN[s[i + 1]] - ROMAN[s[i]]
                i += 2
            else:
                num += ROMAN[s[i]]
                i += 1
        
        if ROMAN[s[len(s) - 1]] <= ROMAN[s[len(s) - 2]]:
            num += ROMAN[s[len(s) - 1]]

        return num

s = 'III'

ob = Solution()

print(ob.romanToInt(s))