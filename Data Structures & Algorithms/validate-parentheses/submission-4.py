class Solution:
    def isValid(self, s: str) -> bool:
        chars = {
            ")": "(",
            "}": "{",
            "]": "["
        }


        stack = []

        for char in s:
            if char not in chars:
                stack.append(char)
            else:
                if stack and stack[-1] == chars[char]:
                    stack.pop()
                else:
                    return False
        
        return not stack