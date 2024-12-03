class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if abs(target - current) < abs(target - closest):
                    closest = current
                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return current
        return closest
