class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        words = s.split()
        for i in range(len(words) - 1, -1, -1):
            ans += words[i] + " "

        return ans.strip()
