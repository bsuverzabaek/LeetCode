class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range((n + 1)//2):
            for j in range(n//2):
                temp = matrix[n - 1 - j][i]
                # Bottom right to bottom left
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                # Top right to bottom right
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                # Top left to top right
                matrix[j][n - 1 - i] = matrix[i][j]
                # Temp to top left
                matrix[i][j] = temp
