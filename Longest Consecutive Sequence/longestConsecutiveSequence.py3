class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        unique = set(nums)
        maxLength = 0

        for num in unique:
            if not num - 1 in unique:
                currentLength = 1

                while num + 1 in unique:
                    num += 1
                    currentLength += 1

                maxLength = max(maxLength, currentLength)

        return maxLength
