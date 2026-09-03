class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        left = 0
        right = len(s1) - 1

        while right < len(s2):
            if self.isPermutation(s2[left: right + 1], s1):
                return True
            left += 1
            right += 1
        
        return False
    
    def isPermutation(self, str1, str2):
        return sorted(str1) == sorted(str2)

