class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        minLength = float("inf")
        currSum = 0

        for right in range(n):
            currSum += nums[right]
            while currSum >= target:
                minLength = min(right - left + 1, minLength)
                currSum -= nums[left]
                left += 1
        
        return minLength if minLength != float('inf') else 0
