class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashmap = new HashMap<>();
        int[] results = new int[2];

        for (int i=0; i < nums.length; i++) {
            int remainder = target - nums[i];
            if (hashmap.containsKey(remainder)) {
                int remainderIndex = hashmap.get(remainder);
                if (i < remainderIndex) {
                    results[0] = i;
                    results[1] = remainderIndex;
                } else {
                    results[0] = remainderIndex;
                    results[1] = i;
                }
            } else {
                hashmap.put(nums[i], i);
            }
        }
        return results;
    }
}
