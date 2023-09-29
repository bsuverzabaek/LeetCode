class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        temp = arr[:2]
        for i in range(2,len(arr)):
            temp.append(arr[i])
            if all(ele%2!=0 for ele in temp)==True:
                return True
            temp.pop(0)
        return False
