class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            "}": "{",
            ")": "(",
            "]": "["
        }

        stack = []

        for char in s:
            if char not in parentheses:
                stack.append(char)
            else:
                if stack and stack[-1] == parentheses[char]:
                    stack.pop()
                else:
                    return False
        
        return not stack



