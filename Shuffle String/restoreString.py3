class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        index = {k:v for k,v in zip(indices,s)}
        return ''.join([index[x] for x in range(len(s))])
