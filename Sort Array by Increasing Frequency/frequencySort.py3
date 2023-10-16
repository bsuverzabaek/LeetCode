class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        index = Counter(nums)
        heap = []
        arr = []
        for i in index:
            heappush(heap,[index[i],-i])
        while heap:
            m,n = heappop(heap)
            for i in range(m):
                arr.append(n*-1)
        return arr
