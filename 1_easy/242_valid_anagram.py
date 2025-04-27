class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) != len(s):
            return False

        # convert s and t into dic where
        # k = char in s/t, v = number of occurrence in string
        s_dic = {}
        t_dic = {}

        for i in range(len(s)):
            if s[i] in s_dic:
                s_dic[s[i]] += 1
            else:
                s_dic[s[i]] = 1
            
            if t[i] in t_dic:
                t_dic[t[i]] += 1
            else:
                t_dic[t[i]] = 1
        
        return s_dic == t_dic # return if dictionaries are equal

        
s = "anagram"
t = "nagaram"

ob = Solution()
print(ob.isAnagram(s, t))