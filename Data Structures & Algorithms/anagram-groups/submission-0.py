class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}

        for c in strs:
            sortedString = "".join(sorted(c))

            if sortedString in anagrams_dict:
                anagrams_dict[sortedString].append(c)
            else:
                anagrams_dict[sortedString] = [c]
        
        return anagrams_dict.values()