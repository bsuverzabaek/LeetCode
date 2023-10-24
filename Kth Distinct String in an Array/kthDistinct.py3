class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        index = Counter(arr)
        count = 0
        ans = None
        for key in index.keys():
            if index[key]==1:
                count += 1
                if count==k:
                    ans = key
        if ans==None:
            return ""
        return ans
