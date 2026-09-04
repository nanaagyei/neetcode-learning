class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float("inf")
        left = 0 
        currSum = 0

        for right in range(len(nums)):
            currSum += nums[right]
            while currSum >= target:
                minLength = min(minLength, right - left + 1)
                currSum -= nums[left]
                left += 1
        
        return minLength if minLength != float('inf') else 0

        
            

        