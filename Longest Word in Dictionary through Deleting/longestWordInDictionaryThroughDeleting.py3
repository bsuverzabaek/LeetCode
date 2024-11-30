class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def isSubsequence(a,b):
            m,n = len(a),len(b)
            pos_a = pos_b = 0

            while pos_a < m and pos_b < n:
                if a[pos_a] == b[pos_b]:
                    pos_b += 1
                pos_a += 1

            return pos_b == n

        ans = ''

        for word in dictionary:
            if isSubsequence(s,word) and (len(ans)<len(word) or (len(ans)==len(word) and ans>word)):
                ans = word

        return ans
