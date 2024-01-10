class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        r = k
        l = 0
        target = Counter(p)
        ans = []
        while r<=len(s):
            occur = Counter(s[l:r])
            if target == occur:
                ans.append(l)
            del occur[s[l]]
            l+=1
            r +=1
        return ans

        