class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target= Counter(s1)
        occur = Counter(s2[:len(s1)])
        if target == occur:
            return True
        l ,r = 0,len(s1)
        while r < len(s2):
            occur[s2[l]] -=1
            if occur[s2[l]] == 0:
                del occur[s2[l]]
            l+=1
            occur[s2[r]] = occur.get(s2[r],0) +1
            r +=1
            if occur == target:
                return True
        return False