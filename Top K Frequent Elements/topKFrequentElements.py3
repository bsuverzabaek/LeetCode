class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        ans = []

        for num, freq in freqDict.items():
            bucket[freq].append(num)

        i = len(bucket) - 1

        while i > 0 and len(ans) < k:
            if bucket[i]:
                for num in bucket[i]:
                    ans.append(num)
            i -= 1

        return ans
