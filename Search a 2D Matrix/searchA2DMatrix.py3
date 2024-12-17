class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        if matrix == None or rows == 0 or cols == 0:
            return False

        left, right = 0, rows * cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            row, col = mid // cols, mid % cols
            midVal = matrix[row][col]

            if midVal == target:
                return True
            elif midVal < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False
