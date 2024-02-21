class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count =0
        ans = 0
        for i in range(len(s))        :
            if s[i]=='(':
                count +=1
            else:
                if count == 0:
                    ans +=1
                else:
                    count -=1
        return ans+count
                    