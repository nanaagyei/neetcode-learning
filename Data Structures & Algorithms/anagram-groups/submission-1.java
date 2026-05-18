class Solution {
    public String sortString(String s) {
        char[] charArray = s.toCharArray();
        
        Arrays.sort(charArray);
        
        String sorted = new String(charArray);

        return sorted;
    }

    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagramsDict = new HashMap<>();

        for (String s : strs) {
            String sortedString = sortString(s);

            anagramsDict.putIfAbsent(sortedString, new ArrayList<>());
            anagramsDict.get(sortedString).add(s);
        }

        return new ArrayList<>(anagramsDict.values());
    }

    
}
