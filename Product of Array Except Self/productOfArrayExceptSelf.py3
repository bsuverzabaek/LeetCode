class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 0:
            return [0]

        prefix, suffix, n, answer = 1, 1, len(nums), []

        for i in range(n):
            answer.append(prefix)
            prefix *= nums[i]

        for i in range(n-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
