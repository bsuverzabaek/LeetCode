class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        if len(s) > 12:
            return ans

        def backtrack(i, dots, ip):
            if i == len(s) and dots == 4:
                ans.append(ip[:-1])
                return

            if dots > 4:
                return

            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"):
                    backtrack(j + 1, dots + 1, ip + s[i:j+1] + ".")

        backtrack(0, 0, "")
        return ans
