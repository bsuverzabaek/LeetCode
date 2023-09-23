class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        val = 0 
        for num in nums:
            val = (val*2+num)%5
            answer.append(val==0)
        return answer
