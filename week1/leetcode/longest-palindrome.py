class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        val = list(count.values())
        val.sort(reverse = True)
        ans = 0
        f = False
        for i in range(len(val)):
            if val[i]%2!=0:
                if f :
                    ans += val[i]-1
                else:
                    ans += val[i]
                    f = True
            else:
                ans += val[i]
        return ans