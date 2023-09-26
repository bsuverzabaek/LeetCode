class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        for i in [n//4,n//2,3*n//4,n]:
            if arr[bisect_left(arr,arr[i])+n//4]==arr[i]:
                return arr[i]
