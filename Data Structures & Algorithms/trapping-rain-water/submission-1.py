class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        maxArea = 0
        leftMax, rightMax = height[left], height[right]

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                maxArea += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                maxArea += rightMax - height[right]
        return maxArea
