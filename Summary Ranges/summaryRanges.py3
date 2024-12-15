class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if len(nums) == 0:
            return ans

        start = nums[0]

        for i in range(1,len(nums)+1,1):
            if i == len(nums) or nums[i] != nums[i-1] + 1:
                if start != nums[i-1]:
                    ans.append(str(start) + "->" + str(nums[i-1]))
                else:
                    ans.append(str(start))
                if i < len(nums):
                    start = nums[i]

        return ans
