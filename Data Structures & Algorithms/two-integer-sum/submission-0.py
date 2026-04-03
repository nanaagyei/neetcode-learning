class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = {}

        for i, num in enumerate(nums):
            if (target - num) in hashNum:
                return [min(i, hashNum[target - num]), max(i, hashNum[target - num])]
            hashNum[num] = i