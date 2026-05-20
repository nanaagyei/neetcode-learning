class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr, L, M, R):
            leftArray, rightArray = arr[L:M + 1], arr[M + 1: R + 1]
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
                i += 1
                j += 1
            
            while k < len(rightArray):
                nums[i] = rightArray[k]
                i += 1
                k += 1
        
        def mergeSort(arr, l, r):
            if l == r:
                return
            
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
            return
        
        mergeSort(nums, 0, len(nums))
        return nums

    

    
