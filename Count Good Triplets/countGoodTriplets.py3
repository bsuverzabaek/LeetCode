class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i,j,k in combinations(arr,3):
            if abs(i-j)<=a and abs(j-k)<=b and abs(k-i)<=c:
                count += 1
        return count
