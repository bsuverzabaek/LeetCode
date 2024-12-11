class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = minProduct = result = nums[0]

        for i in range(1,len(nums)):
            current = nums[i]

            temp = max(current, maxProduct * current, minProduct * current)
            minProduct = min(current, maxProduct * current, minProduct * current)
            maxProduct = temp

            result = max(result, maxProduct)

        return result
