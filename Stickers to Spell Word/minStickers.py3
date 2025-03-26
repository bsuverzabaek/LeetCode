class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        sCount = []
        for i, s in enumerate(stickers):
            sCount.append({})
            for c in s:
                sCount[i][c] = 1 + sCount[i].get(c, 0)

        dp = {} # key: subseq of target, val: min num of stickers

        def helper(t, stick):
            if t in dp:
                return dp[t]

            res = 1 if stick else 0
            remainT = ""

            for c in t:
                if c in stick and stick[c] > 0:
                    stick[c] -= 1
                else:
                    remainT += c

            if remainT:
                used = float("inf")
                
                for s in sCount:
                    if remainT[0] not in s:
                        continue

                    used = min(used, helper(remainT, s.copy()))

                dp[remainT] = used
                res += used

            return res

        res = helper(target, {})
        return res if res != float("inf") else -1
