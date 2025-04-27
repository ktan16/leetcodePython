class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        pairs = {'}':'{', ')':'(', ']':'['}
        
        for c in s:
            if c in pairs:
                if stack and stack[-1] == pairs[c]: # if stack is not empty and last element in stack matches current closing paren
                    stack.pop()
                else: # if stack empty or paren not match
                    return False
                
            else:
                stack.append(c)

        return True if not stack else False

s = '()'
ob = Solution()

print(ob.isValid(s))