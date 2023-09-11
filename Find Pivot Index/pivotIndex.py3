class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = None
        rightSum = None
        ans = []
        for i in range(len(nums)):
            if i==0:
                leftSum = 0
                rightSum = sum(nums[1:])
            else:
                leftSum += nums[i-1]
                rightSum -= nums[i]
            if leftSum==rightSum:
                ans.append(i)
        if len(ans)==0:
            return -1
        return ans[0]
