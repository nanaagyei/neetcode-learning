class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        size_s1 = len(s1)

        for right in range(len(s2)):
            while (right - left + 1) <= size_s1:
                right += 1
            if self.isPermutationOf(s2[left: right], s1):
                return True
            else:
                left += 1
        
        return False
    
    def isPermutationOf(self, str1, str2):
        return "".join(sorted(str1)) == "".join(sorted(str2))
