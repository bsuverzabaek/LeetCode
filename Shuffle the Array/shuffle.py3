class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        temp1 = nums[:n]
        temp2 = nums[n:]
        ans = []
        for x,y in zip(temp1,temp2):
            ans.append(x)
            ans.append(y)
        return ans
