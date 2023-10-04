class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = ' '.join(words)
        ans = [word for word in words if arr.count(word)>=2]
        return ans
