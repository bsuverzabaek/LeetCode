class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans,n = 0,len(arr)
        for i,a in enumerate(arr):
            ans += ((i+1)*(n-i)+1)//2*a
        return ans
