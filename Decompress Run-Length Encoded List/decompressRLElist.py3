# Original Solution
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freqs = []
        vals = []
        ans = []
        for i in range(len(nums)):
            if i%2==0:
                freqs.append(nums[i])
            else:
                vals.append(nums[i])
        for freq,val in zip(freqs,vals):
            for i in range(freq):
                ans.append(val)
        return ans

# Alternative Solution
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(nums),2):
            freq = nums[i]
            val = nums[i+1]
            ans += [val]*freq
        return ans

# One-liner
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        return [x for freq,val in zip(nums[::2],nums[1::2]) for x in [val]*freq]
