class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 0:
            return [[]]

        intervals.sort(key = lambda i : i[0])
        ans = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = ans[-1][1]
            
            if start <= lastEnd:
                ans[-1][1] = max(lastEnd, end)
            else:
                ans.append([start, end])

        return ans
