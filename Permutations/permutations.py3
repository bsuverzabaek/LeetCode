class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permu(nums, current_permu):
            if not nums:
                ans.append(current_permu)
                return
            
            for i in range(len(nums)):
                permu(nums[:i] + nums[i+1:], current_permu + [nums[i]])

        ans = []
        permu(nums, [])
        return ans
