from bisect import bisect_left

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        ans = 0
        n = len(nums)

        for i in range(n-2):
            for j in range(i+1, n-1):
                k = bisect_left(nums,nums[i]+nums[j],lo=j+1) - 1
                ans += k - j

        return ans
