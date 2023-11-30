class Solution(object):
    def checkPowersOfThree(self, n):
        for i in range(17,-1,-1):
            p = 3**i
            if n>= p:
                n -= p
            if n== 0:
                return True
    
        return False