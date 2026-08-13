class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R): # L,  M, R are indexes
            leftArray, rightArray = arr[L : M + 1], arr[M + 1: R + 1]
            i, j, k = L, 0, 0

            while j < len(leftArray) and k < len(rightArray):
                if leftArray[j] <= rightArray[k]:
                    arr[i] = leftArray[j]
                    j += 1
                else:
                    arr[i] = rightArray[k]
                    k += 1
                i += 1

            while j < len(leftArray):
                nums[i] = leftArray[j]
                j += 1
                i += 1
            
            while k < len(rightArray):
                nums[i] = rightArray[k]
                k += 1
                i += 1

            
            
        
        def mergeSort(arr, l, r):
            if l == r:
                return
            
            m = (l + r) // 2 # split in the middle
            mergeSort(arr, l, m) # mergeSort the left array
            mergeSort(arr, m + 1, r) # mergeSort the right array
            merge(arr, l, m, r) # merge the left and right arrays recursively
            return
        
        mergeSort(nums, 0, len(nums))
        return nums
            
        

        