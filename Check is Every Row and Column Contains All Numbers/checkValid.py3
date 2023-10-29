class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        temp = set(range(1,len(matrix)+1))
        return all(temp==set(x) for x in matrix+list(zip(*matrix)))
