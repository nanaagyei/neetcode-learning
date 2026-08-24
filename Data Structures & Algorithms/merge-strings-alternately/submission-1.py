class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left1 = 0
        left2 = 0

        new_str = ""

        while left1 < len(word1) and left2 < len(word2):
            new_str += word1[left1]
            left1 += 1
            new_str += word2[left2]
            left2 += 1
        
        if left1 < len(word1):
            new_str += word1[left1:]
        
        if left2 < len(word2):
            new_str += word2[left2:]
        
        return new_str
