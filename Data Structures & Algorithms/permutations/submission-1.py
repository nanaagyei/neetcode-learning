class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        result = []
        perms = self.permute(nums[1:])

        for p in perms:
            for i in range(len(p) + 1):
                result.append(p[:i] + [nums[0]] + p[i:])
        return result
