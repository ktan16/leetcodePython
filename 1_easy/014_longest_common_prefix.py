class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort() # sort strings alphabetically
        first = strs[0] # compare first and last strings of array
        last = strs[-1]
        
        if len(strs) < 1:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        lcp = ""

        for i in range(len(first)):
            if first[i] == last[i]: # add to lcp while first and last are equal to each other
                lcp += first[i]
            else:
                return lcp
        
        return lcp

    
ob = Solution()

strs = ["a"]
print(ob.longestCommonPrefix(strs))