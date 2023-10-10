class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        i = 0
        j = i+1
        while i<j and j<len(nums):
            if nums[i]==nums[j]:
                count += 1
            if j==len(nums)-1:
                i += 1
                j = i+1
            else:
                j += 1
        return count
