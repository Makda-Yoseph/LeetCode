class Solution(object):
    def totalMoney(self, n):
        sa =0
        if n<=7:
            for i in range(1,n+1):
                sa +=i
        else:
            a = n//7
            sa = (a*(2*28 + (7*(a-1))))/2
            r = n%7
            l= int(a+r+1)
            for i in range(a+1,l):
                sa += i
        return sa
        

        