class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        e ,c,ct = 0,0,0
        while e<len(g) and c<len(s):
            if s[c] >= g[e]:
                ct +=1
                e+=1
                c +=1
                continue
            else:
                c+=1
        return ct
            


        