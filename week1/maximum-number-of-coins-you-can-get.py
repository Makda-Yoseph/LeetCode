class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        your_pile = sorted(piles, reverse = True)
        ma = 0
        ct = 0
        for i in range(1,len(your_pile),2):
            ct +=2
            ma +=your_pile[i]
            if ct/2 == len(your_pile)-ct:
                break
        return ma

        

        