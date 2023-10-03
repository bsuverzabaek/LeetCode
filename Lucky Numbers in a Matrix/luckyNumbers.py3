class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = [min(i) for i in matrix]
        col = []
        ans = []
        for i in range(len(matrix[0])):
            c = [k[i] for k in matrix]
            col.append(max(c))
        for i in row:
            if i in col:
                ans.append(i)
        return ans
