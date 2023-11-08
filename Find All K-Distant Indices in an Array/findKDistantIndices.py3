class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        added = -1
        for i, num in enumerate(nums):
            if num==key:
                ans += range(max(i-k,added+1),min(i+k+1,len(nums)))
                added = ans[-1]
        return ans
