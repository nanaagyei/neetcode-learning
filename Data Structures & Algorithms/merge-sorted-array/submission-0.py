class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = 0
        while m < len(nums1):
            nums1[m] = nums2[left]
            left += 1
            m += 1

        nums1.sort() 