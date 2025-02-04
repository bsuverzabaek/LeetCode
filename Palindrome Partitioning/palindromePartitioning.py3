class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        partition = []

        def backtrack(i):
            if i >= len(s):
                result.append(partition.copy())
                return

            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    partition.append(s[i:j+1])
                    backtrack(j+1)
                    partition.pop()

        backtrack(0)
        return result

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1

        return True
