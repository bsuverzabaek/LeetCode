class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        
        for i in range(numRows):
            row = []
            
            for j in range(i+1):
                row.append(1)
            
            for j in range(1,i):
                valueAboveLeft = ans[i-1][j-1]
                valueAboveRight = ans[i-1][j]
                sum = valueAboveLeft + valueAboveRight
                row[j] = sum
            
            ans.append(row)

        return ans
