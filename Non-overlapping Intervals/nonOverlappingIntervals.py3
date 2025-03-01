class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        result = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                result += 1
                if end < prevEnd:
                    prevEnd = end

        return result
