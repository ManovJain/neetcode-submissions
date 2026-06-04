class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenPairs = {
            '}' : '{',
            ']' : '[',
            ')' : '('
            }
        
        for c in s:
            if c in parenPairs and stack:
                check = stack[-1]
                if check == parenPairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0