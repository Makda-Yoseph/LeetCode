class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occur = dict((a,i) for i,a in enumerate(s))
        print(occur)
        l = 0
        m = 0
        ans = []
        for r in range(len(s)):
            if occur[s[r]] > m:
               m = occur[s[r]] 
            if r == m:
                ans.append(r-l+1)
                l = r+1

        return ans