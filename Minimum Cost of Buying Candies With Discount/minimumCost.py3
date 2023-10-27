# Original Solution
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ans = 0
        while cost:
            ans += cost.pop()
            if len(cost)==0:
                break
            ans += cost.pop()
            if len(cost)==0:
                break
            cost.pop()
        return ans

# Better Solution
class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ans = 0
        for i in range(len(cost)):
            if i%3!=len(cost)%3:
                ans += cost[i]
        return ans
