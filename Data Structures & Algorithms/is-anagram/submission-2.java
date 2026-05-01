class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        Map<String, Integer> countS = new HashMap<>();
        Map<String, Integer> countT = new HashMap<>();

        for (int i=0; i < s.length(); i++) {
            countS.merge(Character.toString(s.charAt(i)), 1, Integer::sum);
            countT.merge(Character.toString(t.charAt(i)), 1, Integer::sum);
        }

        boolean isAnagram = countS.equals(countT);
        return isAnagram;
    }
}
