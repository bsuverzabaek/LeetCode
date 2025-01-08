class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, index, i, j):
            if index == len(word):
                return True

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or board[i][j] != word[index]:
                return False

            temp = board[i][j]
            board[i][j] = "#"

            found = dfs(board, word, index + 1, i + 1, j) or dfs(board, word, index + 1, i - 1, j) or dfs(board, word, index + 1, i, j + 1) or dfs(board, word, index + 1, i, j - 1)

            board[i][j] = temp
            return found

        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(board, word, 0, i, j):
                    return True

        return False
