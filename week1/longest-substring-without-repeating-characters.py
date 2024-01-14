class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occur = {}
        l,r = 0,0
        ma = 0
        while r<len(s):
            occur[s[r]] = occur.get(s[r],0)+1
            if occur[s[r]]>1:
                ma = max(ma,r-l)
                while occur[s[r]]>1:
                    occur[s[l]] -=1
                    if occur[s[l]]== 0:
                        del occur[s[l]]
                    l+=1
            r +=1
        ma = max(ma,r-l)
        return ma

        

            
        