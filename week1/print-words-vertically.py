class Solution(object):
    def printVertically(self,s):
        arr = sorted(list(s.split()), key = len)
        ah = list(s.split())
        n = []
        for i in range(len(arr[-1])):
            alp = ""
            for j in range(len(ah)):
                if i < len(ah[j]):
                    alp += ah[j][i]
                else:
                    alp += " "
            n.append(alp.rstrip())
        return n
            
            
                


        