from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # create dictioary with default value as list
        # key = sorted s in str, value = list of words with same key
        # ex: { 'aet' : ['eat', 'tea', 'ate']}
        res = defaultdict(list)
        
        # loop through each word in list
        for s in strs:
            # sort word, then use it as key
            # append the actual word to the list of other words with the same key
            res["".join(sorted(s))].append(s)
        
        return res.values()
        

ob = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]

print(ob.groupAnagrams(strs))