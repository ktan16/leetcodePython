class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        arr = []
        for str in strs:
            dic = {}
            for c in str:
                if c in dic:
                    dic[c] += 1
                else:
                    dic[c] = 1
            
            arr.append(dic)
        
        print(arr)

ob = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]

print(ob.groupAnagrams(strs))