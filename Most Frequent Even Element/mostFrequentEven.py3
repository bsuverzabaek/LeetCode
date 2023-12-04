class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        index = {}
        for num in nums:
            if num%2==0:
                if num not in index:
                    index[num] = 1
                else:
                    index[num] += 1
        if len(index)==0:
            return -1
        ans = -1
        count = -1
        for key in index.keys():
            if index[key]>count:
                ans = key
                count = index[key]
        return ans
