class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, ans = set(), set()
        L, R = 0, 10

        while R <= len(s):
            curr = s[L:R]
            if curr in seen:
                ans.add(curr)
            seen.add(curr)
            L += 1
            R += 1

        return list(ans)
