class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        first = strs[0]
        last = strs[-1]
        
        if len(strs) < 1:
            return ""
        
        if first[0] != last [0]:
            return ""
        
        lcp = ""

        for i in range(len(first)):
            if first[i] == last[i]:
                lcp += first[i]
            else:
                break
        
        return lcp

    
ob = Solution()

strs = ["a"]
print(ob.longestCommonPrefix(strs))