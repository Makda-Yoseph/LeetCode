class Solution(object):
    def numberOfMatches(self, n):
        t = n
        tm = 0
        while t > 1:
            if n % 2 == 0:
                m = n/2
                t = n/2
            else:
                m = (n-1)/2
                t = ((n-1)/2) + 1
            tm += m
            n = t
        return tm


        