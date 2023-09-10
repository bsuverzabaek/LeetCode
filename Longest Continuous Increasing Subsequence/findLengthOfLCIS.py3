class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        else:
            count = 1
            maxNum = 1
            for i in range(len(nums)-1):
                if nums[i+1]>nums[i]:
                    count += 1
                else:
                    maxNum = max(maxNum,count)
                    count = 1
                if i==len(nums)-2:
                    maxNum = max(maxNum,count)
            return maxNum
