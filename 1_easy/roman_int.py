class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ROMAN = {
            "I":1, "V":5, "X":6, "L":50, "C":100, "D":500, "M":1000
        }

        num = 0
        i = len(s) - 1
        


        
