class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.biSearch(nums, target, True)
        right = self.biSearch(nums, target, False)

        return [left, right]

    def biSearch(self, nums, target, leftBias):
        left, right = 0, len(nums) - 1
        i = -1

        while left <= right:
            mid = left + ((right - left) // 2)

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                i = mid
                if leftBias:
                    right = mid - 1
                else:
                    left = mid + 1

        return i
