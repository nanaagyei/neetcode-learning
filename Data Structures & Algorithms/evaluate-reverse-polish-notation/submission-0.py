class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if not tokens:
            return 0

        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            elif char == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(char))
        return stack[0]