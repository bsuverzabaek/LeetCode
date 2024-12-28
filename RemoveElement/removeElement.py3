class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        validIndex = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[validIndex], nums[i] = nums[i], nums[validIndex]
                validIndex += 1
        return validIndex
