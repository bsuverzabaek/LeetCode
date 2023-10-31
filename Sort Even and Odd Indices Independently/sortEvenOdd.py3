class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        if len(nums)<=2:
            return nums
        evens = []
        odds = []
        for i in range(len(nums)):
            if i%2==0:
                evens.append(nums[i])
                nums[i] = 1
            else:
                odds.append(nums[i])
                nums[i] = 0
        evens.sort(reverse=True)
        odds.sort()
        for i in range(len(nums)):
            if nums[i]==1:
                nums[i] = evens.pop()
            else:
                nums[i] = odds.pop()
        return nums
