class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        index = Counter(nums)
        a = nums[0]
        b = nums[0]
        ans = 0
        for i in range(len(nums)):
            if nums[i]-b==1:
                a = nums[i]
                if i==len(nums)-1:
                    ans = max(ans,index[a]+index[b])
            elif nums[i]-b>1:
                if a-b==1:
                    ans = max(ans,index[a]+index[b])
                a = nums[i]
                b = nums[i-1]
                if i==len(nums)-1 and a-b==1:
                    ans = max(ans,index[a]+index[b])
        return ans
