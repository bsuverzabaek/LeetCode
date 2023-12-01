class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        ene,exp = 0,0
        ene2,exp2 = 0,0
        for en,xp in zip(energy,experience):
            if en>=ene:
                ene2 += (en-ene+1)
                ene += (en-ene+1)
            if xp>=exp:
                exp2 += (xp-exp+1)
                exp += (xp-exp+1)
            ene -= en
            exp += xp
        return max(0,(ene2-initialEnergy))+max(0,(exp2-initialExperience))
