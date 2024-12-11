class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        currentRow, goingDown = 0, False
        rows = [''] * numRows

        for char in s:
            rows[currentRow] += char
            if currentRow == 0 or currentRow == numRows - 1:
                goingDown = not goingDown
            
            currentRow += 1 if goingDown else -1 

        return ''.join(rows)
