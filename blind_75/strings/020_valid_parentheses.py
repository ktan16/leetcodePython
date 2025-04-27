class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'}':'{', ')':'(', ']':'['}

        for paren in s:

            # if this is a closing paren
            if paren in pairs:
                # if the stack is not empty and the most recently added is the pair
                if stack and stack[-1] == pairs[paren]:
                    # remove the matching open paren from stack
                    stack.pop()
                else:
                    # stack is empty or most recent paren is not the opening pair
                    return False
                
            # only add open parens
            else:
                stack.append(paren)

        # stack must be empty to be true
        return True if not stack else False

s = "([][))"

ob = Solution()
print(ob.isValid(s))