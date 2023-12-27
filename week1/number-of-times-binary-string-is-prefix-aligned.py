class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n= len(flips)
        s = [0]*n
        count = 0
        k = 0
        # for i in flips:
        #     k +=1
        #     s[i-1] = 1
        #     c = [1]*k

        #     if s[:k] == c:
        #         count +=1
        for i in range(n):
            s[flips[i]-1] = 1
            if flips[i]-1 < i :
                k+=1
            if s[i] ==1:
                k +=1
            if k == i+1:
                count +=1
        return count

        