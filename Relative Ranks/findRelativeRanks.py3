class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        answer = []
        index = {}
        score2 = sorted(score,reverse=True)
        for i in range(len(score2)):
            if i==0:
                index[score2[i]] = "Gold Medal"
            elif i==1:
                index[score2[i]] = "Silver Medal"
            elif i==2:
                index[score2[i]] = "Bronze Medal"
            else:
                index[score2[i]] = str(i+1)
        for i in score:
            answer.append(index[i])
        return answer
