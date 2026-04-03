class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        left = 0

        countT, window = {}, {}
        
        for char in t:
            countT[char] = 1 + countT.get(char, 0)
        
        res, resLen = [-1, -1], float("infinity")
        have = 0
        need = len(countT)

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                
                left += 1
        left, right = res

        return s[left: right + 1] if resLen != float("infinity") else ""

        
        