class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = len(s1) - 1

        while right < len(s2):
            if self.isPermutation(s1, s2[left: right + 1]):
                return True
            left += 1
            right += 1
        
        return False

    

    def isPermutation(self, str1: str, str2: str) -> bool:
        return sorted(str1) == sorted(str2)