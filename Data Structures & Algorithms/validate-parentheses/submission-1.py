class Solution:
    def isValid(self, s: str) -> bool:
        par_dict = {
            "(":")",
            "{":"}",
            "[":"]"
        }

        stack = []
        for char in s:
            if char in par_dict:
                stack.append(char)
            else:
                if stack and par_dict[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        return not stack

    