class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1))-sum(nums)

# Original Solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(min(nums),n+1):
            if i not in nums:
                return i
