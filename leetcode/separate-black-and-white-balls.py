class Solution:
    def minimumSteps(self, s: str) -> int:
        r = len(s)-1
        ctz = 0
        ct = 0
        for i in range(len(s)):
            if s[r] == '0':
                ctz +=1
            elif s[r] == '1':
                ct +=ctz
            r -=1
        return ct
                

        