class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = (top + bottom) // 2

            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                break

        if top > bottom:
            return False
        
        left = 0
        right = len(matrix[0]) - 1
        row = (top + bottom) // 2

        while left <= right:
            m = (left + right) // 2

            if target < matrix[row][m]:
                right = m - 1
            elif target > matrix[row][m]:
                left = m + 1 
            else:
                return True
        
        return False