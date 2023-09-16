# First Solution
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num%2==0:
                ans.append(num)
        for num in nums:
            if num%2!=0:
                ans.append(num)
        return ans

# Second Solution
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for num in nums:
            if num%2==0:
                even.append(num)
            else:
                odd.append(num)
        return even+odd
