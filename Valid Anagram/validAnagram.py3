class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = Counter(s)

        for char in t:
            countS[char] -= 1

            if countS[char] < 0:
                return False

        return True
