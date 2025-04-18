class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while True:
            mid = left + ((right - left) // 2)
            res = guess(mid)

            if res == 0:
                return mid
            elif res > 0:
                left = mid + 1
            else:
                right = mid - 1
