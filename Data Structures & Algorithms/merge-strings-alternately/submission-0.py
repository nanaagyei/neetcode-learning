class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left1 = 0
        left2 = 0
        mergedString = ""

        while left1 < len(word1) and left2 < len(word2):
            mergedString += word1[left1]
            mergedString += word2[left2]
            left1 += 1
            left2 += 1

        mergedString += word1[left1:] if left1 < len(word1) else word2[left2:]

        return mergedString

