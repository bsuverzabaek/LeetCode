class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        for a,b in pairwise(nums):
            if (t:=a+b) in seen:
                return True
            else:
                seen.add(t)
        return False
