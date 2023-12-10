class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        s=set(nums)
        for num in nums:
            if 0-num in s:
                return num
        return -1
