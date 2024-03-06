# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        ans = 0
        mid = 0
        higher,lower = n,1
        while higher>=lower:
            mid= (higher+lower)//2
            g = (guess(mid))
            if g ==0:
                return mid
            elif g==-1:
                higher = mid-1
            elif g == 1:
                lower = mid +1
            
        