class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        left = 0

        for right in range(k - 1, len(nums)):
            if right + 1 < len(nums):
                subarray = nums[left: right + 1]
                
            else:
                subarray = nums[left:]
            
            output.append(max(subarray))
            
            left += 1
        return output
