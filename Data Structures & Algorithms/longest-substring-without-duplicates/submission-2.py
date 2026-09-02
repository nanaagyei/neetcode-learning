class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        stringSet = set()

        for right in range(len(s)):
            while s[right] in stringSet:
                stringSet.remove(s[left])
                left += 1

            maxLength = max(maxLength, right - left + 1)
            
            stringSet.add(s[right])
        
        return maxLength

