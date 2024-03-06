class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        h = ceil(x/2)
        while l <= h:
            mid = ( l + h ) // 2
            if mid * mid  == x:
                return mid
            elif mid * mid < x:
                l = mid+1
            else:
                h = mid -1
        return h
        


        