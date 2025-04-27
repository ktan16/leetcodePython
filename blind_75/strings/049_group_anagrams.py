from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # k:v = any:list
        ans = defaultdict(list)

        for str in strs:
            # sort str, returns list so join list values into string
            s = "".join(sorted(str))
            # append actual string to list
            ans[s].append(str)
        
        # return only the values which contains grouped anagrams
        return ans.values()
    
strs = ["eat","tea","tan","ate","nat","bat"]

ob = Solution()
print(ob.groupAnagrams(strs))