class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, total = 0, 0, 0
        ans = len(nums) + 1

        while right < len(nums):
            total += nums[right]
            while total >= target:
                if right - left + 1 < ans:
                    ans = right - left + 1

                total -= nums[left]
                left += 1

            right += 1

        return 0 if ans == len(nums) + 1 else ans
