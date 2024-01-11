class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        occur = {'a':0, 'e':0, 'i':0, 'o':0,'u':0}
        for i in range(k):
            if s[i] in occur:
                occur[s[i]] +=1
        ma = 0
        v = sum(occur.values())
        ma = max(ma,v)
        l ,r = 0,k
        while r < len(s):
            if s[r] in  occur:
                occur[s[r]] +=1
            if s[l] in occur:
                occur[s[l]] -=1
            l+=1
            r +=1
            v = sum(occur.values())
            ma = max(ma,v)
        v = sum(occur.values())
        ma = max(ma,v)
        return ma
        