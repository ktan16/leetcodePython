class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {char: 0 for char in s}
        t_map = {char: 0 for char in t}

        for i in range(len(s)):
            s_map[s[i]] += 1
            t_map[t[i]] += 1

        return s_map == t_map
    
s = "rat"
t = "art"

ob = Solution()
print(ob.isAnagram(s, t))