class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in "+-*/":
                stack.append(int(char))
            else:
                opera1, opera2 = stack.pop(), stack.pop()
                if char == "+":
                    stack.append(opera2+opera1)
                elif char == "-":
                    stack.append(opera2-opera1)
                elif char == "*":
                    stack.append(opera2*opera1)
                else:
                    stack.append(int(float(opera2)/opera1))
        return stack.pop()