class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0

        while left < len(nums):
            for right in range(left + 1, len(nums)):
                if nums[left] == nums[right] and abs(left - right) <= k:
                    return True
            
            left += 1
        
        return False


        