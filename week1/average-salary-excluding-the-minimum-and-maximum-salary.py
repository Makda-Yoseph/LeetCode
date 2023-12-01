class Solution(object):
    def average(self, salary):
        n = len(salary)
        x = sorted(salary)
        d = 0
        for s in x:
            d += s
        d = d - x[0]
        d = d - x[n-1]
        avg = float(d) / float(n-2)
        return avg