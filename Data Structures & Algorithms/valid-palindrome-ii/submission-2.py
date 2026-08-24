class Solution:
    def validPalindrome(self, s: str) -> bool:
        new_str = ""

        for i in range(len(s)):
            new_str = s[:i] + s[i+1:]
            if self.isPalindrome(new_str):
                return True
        
        return False
        

    
    def isPalindrome(self, s:str) -> bool:
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left].lower() != s[right].lower():
                return False
            
            left, right = left + 1, right - 1
        
        return True