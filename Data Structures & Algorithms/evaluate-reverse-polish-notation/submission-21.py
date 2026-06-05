class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ["+", "-", "*", "/"]

        for i in tokens:
            if i in operands:
                num2 = stack.pop()
                num1 = stack.pop()
                if i == "+":
                    stack.append(num1 + num2)
                elif i == "-":
                    stack.append(num1 - num2)
                elif i == "*":
                    stack.append(num1 * num2)
                elif i == "/":
                    stack.append(int(float(num1) / num2))
            else:
                stack.append(int(i))
            print(stack)
            
        return stack.pop()

