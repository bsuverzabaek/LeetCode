class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        index = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if nums[i][j] not in index:
                    index[nums[i][j]] = 1
                else:
                    index[nums[i][j]] += 1
        ans = []
        for key in index.keys():
            if index[key]==len(nums):
                ans.append(key)
        return sorted(ans)
