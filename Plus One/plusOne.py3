# Original Solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ""
        temp2 = None
        ans = []
        for i in digits:
            temp += str(i)
        temp2 = int(temp)+1
        for i in str(temp2):
            ans.append(int(i))
        return ans

# Better Solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i] += 1
                return digits
        return [1]+digits
