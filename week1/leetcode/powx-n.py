class Solution:
    def myPow(self, x: float, n: int) -> float:
        def exp(x,n):
            if n == 0:
                return 1
            z = n//2
            r = n%2
            
            if r:
                res = self.myPow(x,abs(z))
                return res*res*x
            else:
                res = exp(x,abs(z))
                return res*res
        result = exp(x,abs(n))
        if n<0:
            return 1/result
        return result
            