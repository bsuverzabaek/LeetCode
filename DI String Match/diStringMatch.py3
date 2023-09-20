class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        temp = [i for i in range(0,len(s)+1)]
        ans = []
        for i in s:
            if i=='I':
                ans.append(temp.pop(0))
            if i=='D':
                ans.append(temp.pop())
        ans.append(temp.pop())
        return ans
