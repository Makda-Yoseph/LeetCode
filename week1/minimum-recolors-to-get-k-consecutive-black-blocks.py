class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ct = 0
        for i in range(k):
            if blocks[i] == 'W':
                ct +=1
        m = ct
        l = 0
        r = k
        while r<len(blocks):
            if blocks[l] == 'W':
                ct -=1
            if blocks[r] == 'W':
                ct +=1
            l+=1
            r +=1
            m = min(m,ct)
        return m
            


        