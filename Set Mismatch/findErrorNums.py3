class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s1 = sum(nums)
        s2 = sum(set(nums))
        s3 = (n*(n+1))//2
        return [s1-s2,s3-s2]
