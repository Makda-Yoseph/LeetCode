class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occur = {}
        mx,ma = 0,0
        r,l = 0,0
        while r<len(s):
            occur[s[r]] = occur.get(s[r],0)+1
            ma = max(ma,occur[s[r]])
            # mx = max(occur.values())
            # t = abs(sum(occur.values())-mx)
            while (r-l+1)-ma >k :
                occur[s[l]]-=1
                l+=1
            
            mx = max(mx,r-l+1)
            r+=1
        return mx

        