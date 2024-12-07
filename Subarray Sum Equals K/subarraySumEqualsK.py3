class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Initialize with prefix sum 0 and count 1 to handle cases where subarrays start from the beginning
        prefixSumCount = {0: 1}
        prefixSum = 0
        count = 0

        for num in nums:
            prefixSum += num
            if (prefixSum - k) in prefixSumCount:
                count += prefixSumCount[prefixSum - k]
            if prefixSum in prefixSumCount:
                prefixSumCount[prefixSum] += 1
            else:
                prefixSumCount[prefixSum] = 1

        return count
