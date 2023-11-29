class Solution(object):
    def smallestEvenMultiple(self, n):
        r = n*2
        for i in range(1,r+1):
            if i%n == 0 and i%2 == 0 and i<r:
                r = i
        return r

        