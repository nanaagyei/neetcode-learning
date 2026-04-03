class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]

        maxSum = 0
        for n in nums:
            maxSum += n
            res = max(maxSum, res)
            if maxSum < 0:
                maxSum = 0
        return res

            
