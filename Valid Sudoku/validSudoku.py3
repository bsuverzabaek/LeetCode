class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        checker = set()

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    if num + " in row " + str(i) in checker or num + " in column " + str(j) in checker or num + " in block " + str(i//3) + "-" + str(j//3) in checker:
                        return False
                    
                    checker.add(num + " in row " + str(i))
                    checker.add(num + " in column " + str(j))
                    checker.add(num + " in block " + str(i//3) + "-" + str(j//3))

        return True
