class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}

        for s in strs:
            sortedString = "".join(sorted(s))

            if sortedString in anagramDict:
                anagramDict[sortedString].append(s)
            else:
                anagramDict[sortedString] = [s]
        
        return list(anagramDict.values())
