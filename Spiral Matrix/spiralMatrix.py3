class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return ans

        rows, cols = len(matrix), len(matrix[0])
        up, down, left, right = 0, rows - 1, 0, cols - 1

        while up <= down and left <= right:
            for col in range(left, right + 1):
                ans.append(matrix[up][col])

            for row in range(up + 1, down + 1):
                ans.append(matrix[row][right])

            if up != down:
                for col in range(right - 1, left - 1, -1):
                    ans.append(matrix[down][col])

            if left != right:
                for row in range(down - 1, up, -1):
                    ans.append(matrix[row][left])

            up += 1
            down -= 1
            left += 1
            right -= 1

        return ans
