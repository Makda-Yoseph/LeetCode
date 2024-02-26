class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        if n%2:
            return(pow(5,ceil(n/2),10**9+7)*pow(4,n//2,10**9+7))%(10**9+7)
        else:
            return(pow(5,(n//2),10**9+7)*pow(4,n//2,10**9+7))%(10**9+7)
        