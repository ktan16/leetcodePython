class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed = "".join(char for char in s if char.isalnum())

        return trimmed.lower() == trimmed[::-1].lower()
    
s = "A man, a plan, a canal: Panama"

ob = Solution()
print(ob.isPalindrome(s))