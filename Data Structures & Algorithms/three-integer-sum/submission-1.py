class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        threeSums = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + num
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    threeSums.append([nums[left], nums[right], num])
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        return threeSums


        