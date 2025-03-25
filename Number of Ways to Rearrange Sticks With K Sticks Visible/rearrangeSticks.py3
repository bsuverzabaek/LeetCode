class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = {}

        def helper(N, K):
            if N == K:
                return 1

            if N == 0 or K == 0:
                return 0

            if (N, K) in dp:
                return dp[(N, K)]

            dp[(N, K)] = (helper(N - 1, K - 1) + (N - 1) * helper(N - 1, K)) % (10**9 + 7)
            return dp[(N, K)]

        return helper(n, k)
