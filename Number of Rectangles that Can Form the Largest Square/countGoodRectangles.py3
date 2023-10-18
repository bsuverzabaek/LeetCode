class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = 0
        m = 0
        for l,w in rectangles:
            side = min(l,w)
            if side>m:
                count = 1
                m = side
            elif side==m:
                count += 1
        return count
