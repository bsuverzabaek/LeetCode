class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = newSum = sum(nums[:k])
        for i in range(k,len(nums)):
            current += nums[i]-nums[i-k]
            newSum = max(newSum,current)
        return newSum/k
