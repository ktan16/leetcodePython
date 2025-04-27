class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1
            letters.add(s[right])
            longest = max(longest, right - left + 1)
        
        return longest

s = "pwwkew"

ob = Solution()
print(ob.lengthOfLongestSubstring(s))