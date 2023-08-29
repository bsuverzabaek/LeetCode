# Original Solution
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        first = set('qwertyuiop')
        second = set('asdfghjkl')
        third = set('zxcvbnm')
        for word in words:
            temp = set(word.lower())
            if temp<=first or temp<=second or temp<=third:
                ans.append(word)
        return ans

# Better Solution
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = (set('qwertyuiop'),set('asdfghjkl'),set('zxcvbnm'))
        return [word for word in words if any(set(word.lower()).issubset(row) for row in rows)]
