class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = ans = total = 0

        for right in range(len(nums)):
            total += nums[right]

            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1

            if right - left + 1 > ans:
                ans = right - left + 1

        return ans
