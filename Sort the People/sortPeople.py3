class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        index = dict(zip(heights,names))
        ans = []
        heights.sort(reverse=True)
        for height in heights:
            ans.append(index[height])
        return ans
