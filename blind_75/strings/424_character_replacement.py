class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0

        # init map with characters and each count = 0
        letters = {letter: 0 for letter in s}

        for right in range(len(s)):
            # update count for character
            letters[s[right]] += 1

            # if window length - biggest count of any char > k
            # ran out of replacements, cannot iterate right
            # iterate left so that k is satisfied again
            while (right - left + 1) - max(letters.values()) > k:
                letters[s[left]] -= 1
                left += 1
            
            longest = max(longest, right - left + 1)

        return longest
    
s = "aababba"
k = 1

ob = Solution()
print(ob.characterReplacement(s,k))