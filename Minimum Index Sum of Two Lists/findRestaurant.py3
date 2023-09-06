class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        set1 = set(list1)&set(list2)
        leastSum = 1000000
        for word in set1:
            currentSum = list1.index(word)+list2.index(word)
            if currentSum<leastSum:
                ans.clear()
                ans.append(word)
                leastSum = currentSum
            elif currentSum==leastSum:
                ans.append(word)
        return ans
