class Solution: 
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)

        def reverse(nums: List[int], start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)
