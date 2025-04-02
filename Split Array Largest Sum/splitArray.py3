class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 0
            curr = 0

            for num in nums:
                curr += num
                if curr > largest:
                    subarray += 1
                    curr = num

            return subarray + 1 <= k

        left, right = max(nums), sum(nums)
        res = right

        while left <= right:
            mid = left + ((right - left) // 2)

            if canSplit(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
