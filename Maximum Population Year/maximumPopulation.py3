class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = []
        for birth,death in logs:
            years.append((birth,1))
            years.append((death,-1))
        years.sort()
        pop = 0
        maxPop = 0
        maxYear = 0
        for year,change in years:
            pop += change
            if pop>maxPop:
                maxPop = pop
                maxYear = year
        return maxYear
