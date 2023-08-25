class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        if len(s)<3:
            return max(nums)
        a = list(s)
        a.sort(reverse=True)
        return a[2]
