class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        s = list(palindrome)
        if len(s) == 1:
            return ""
        f = 0
        for i in range(len(s)):
            if len(s)%2 != 0 and i == len(s)//2:
                continue
        
            if s[i]!= 'a':
                s[i] = 'a'
                f = 1
                break
        if f:
            return (''.join(s))
        else:
            s[-1]='b'
            return (''.join(s))
                
            