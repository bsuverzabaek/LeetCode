class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        sum = nums[0]
        ans = 0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                sum += nums[i]
            else:
                ans = max(ans,sum)
                sum = nums[i]
        ans = max(ans,sum)
        return ans
