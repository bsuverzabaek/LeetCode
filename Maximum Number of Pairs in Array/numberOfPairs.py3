class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        index = Counter(nums)
        ans = [0,0]
        for key in index.keys():
            ans[0] += index[key]//2
            ans[1] += index[key]%2
        return ans
