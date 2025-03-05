class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        queue = collections.deque()
        left = right = 0

        while right < len(nums):
            # Pop smaller values from queue
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()

            queue.append(right)

            # Remove left value from window
            if left > queue[0]:
                queue.popleft()

            if (right + 1) >= k:
                ans.append(nums[queue[0]])
                left += 1

            right += 1

        return ans
