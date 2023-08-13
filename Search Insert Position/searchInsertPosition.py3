class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = None
        if nums[0]==target or target<nums[0]:
            ans = 0
        else:
            for i in range(1,len(nums)):
                if nums[i]==target:
                    ans = i
                    break
                if target>nums[i-1] and target<nums[i]:
                    ans = i
                    break
        if ans==None:
            ans = len(nums)
        return ans
