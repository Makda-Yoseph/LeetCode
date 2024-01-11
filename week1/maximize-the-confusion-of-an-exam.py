class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        l,r,ma ,ct = 0,0,0,0
        occur = {'T':0,'F':0}
        while r <len(answerKey):
            if min(occur.values()) <= k:
                occur[answerKey[r]] +=1
                if min(occur.values()) >k:
                    d = r-l
                    ma = max(d,ma)
                    while min(occur.values()) >k:
                        occur[answerKey[l]] -=1
                        l+=1
            r +=1
            
        d = r-l
        ma = max(ma,d)
        return ma