class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        ans, x = 0, abs(x)

        while x:
            x, mod = divmod(x, 10)
            ans = ans * 10 + mod

            if ans > 2**31 - 1:
                return 0

        return ans * sign
