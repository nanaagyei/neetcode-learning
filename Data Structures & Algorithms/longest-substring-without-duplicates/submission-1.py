class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        stringSet = set()
        res = 0

        for right in range(len(s)):
            while s[right] in stringSet:
                stringSet.remove(s[left])
                left += 1
            res = max(res, right - left + 1)

            stringSet.add(s[right])

        return res
