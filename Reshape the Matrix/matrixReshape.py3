class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (len(mat)*len(mat[0])) != r*c:
            return mat
        else:
            ans = []
            temp = []
            row = 0
            col = 0
            for i in range(len(mat)):
                if row >= r:
                    row = 0
                    continue
                for j in range(len(mat[i])):
                    temp.append(mat[i][j])
                    col += 1
                    if col >= c:
                        ans.append(temp)
                        temp = []
                        col = 0
                        row += 1
            return ans
