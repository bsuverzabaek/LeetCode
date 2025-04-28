class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right]:
                if nums[left] < ans:
                    ans = nums[left]
                break

            mid = left + ((right - left) // 2)
            
            if nums[mid] < ans:
                ans = nums[mid]

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return ans
