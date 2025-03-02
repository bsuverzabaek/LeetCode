class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tCount, window = {}, {}

        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)

        have, need = 0, len(tCount)
        ans, ansLen = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            if c in tCount and window[c] == tCount[c]:
                have += 1

            while have == need:
                # update result
                if (right - left + 1) < ansLen:
                    ans = [left, right]
                    ansLen = (right - left + 1)

                # move window left
                window[s[left]] -= 1
                if s[left] in tCount and window[s[left]] < tCount[s[left]]:
                    have -= 1
                left += 1

        left, right = ans
        return s[left:right + 1] if ansLen != float("inf") else ""
