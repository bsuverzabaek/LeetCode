class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = []

        for eff, spd in zip(efficiency, speed):
            engineers.append([eff, spd])

        engineers.sort(reverse=True)

        ans, speed = 0, 0
        minHeap = []

        for eff, spd in engineers:
            if len(minHeap) == k:
                speed -= heapq.heappop(minHeap)

            speed += spd
            heapq.heappush(minHeap, spd)
            ans = max(ans, eff * speed)

        return ans % (10**9 + 7)
