# Original Solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        else:
            neg = False
            temp = [0]*60000
            for i in range(len(nums)):
                if nums[i]<0:
                    neg = True
                temp[nums[i]] += 1
            if neg and temp.index(1)>=30000:
                return temp.index(1)-60000
            else:
                return temp.index(1)

# Better Solution
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans
