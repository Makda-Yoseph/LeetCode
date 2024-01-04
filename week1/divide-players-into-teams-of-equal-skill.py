class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l,r = 0,len(skill)-1
        cr= skill[l] + skill[r] 
        sa = 0
        p = 0
        while l< r:
            if skill[l] + skill[r] != cr:
                return -1

            p =  skill[l] * skill[r]
            sa +=p
            r -=1
            l+=1
        return sa  