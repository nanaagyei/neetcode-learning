class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {} # {num: index}
        result = []

        for i, num in enumerate(nums):
            if (target - num) in nums_dict:
                j = nums_dict[target - num]
                if i <= j:
                    result += [i, j]
                else:
                    result += [j, i]
            nums_dict[num] = i
        
        return result

