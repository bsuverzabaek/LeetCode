class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = []
        nums.append(0)
        if n==0:
            return nums[0]
        nums.append(1)
        i = 1
        while len(nums)<n+1:
            nums.append(nums[i])
            if len(nums)==n+1:
                break
            nums.append(nums[i]+nums[i+1])
            i += 1
        return max(nums)
