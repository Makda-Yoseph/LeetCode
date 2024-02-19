class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        countS = defaultdict(int)
        l = r = 0
        minsize = float('inf')
        ans = ""
        while r < len(s):
            if s[r] in countT:
                countS[s[r]] +=1
            while all(countS[c]>= countT[c] for c in countT) and l<=r:
                curr = r-l+1
                if curr < minsize:
                    minsize = curr
                    ans = s[l:r+1]
                countS[s[l]] -=1
                l+=1
            r+=1
        return ans

        