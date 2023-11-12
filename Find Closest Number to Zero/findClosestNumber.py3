class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 1000000
        for num in nums:
            if abs(0-num)<=abs(0-ans):
                ans = num
        return ans
