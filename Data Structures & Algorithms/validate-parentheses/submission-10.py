class Solution:
    def isValid(self, s: str) -> bool:
        
        #quick check - s length must be even to have valid parens
        if len(s) % 2 != 0:
            return False


        stack = []
        parenPairs = {
            '}' : '{',
            ']' : '[',
            ')' : '('
            }
        
        for c in s:
            if c in parenPairs:
                if not stack or stack.pop() != parenPairs[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0