class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        cost = sorted(costs)
        ma = 0
        ct = 0
        for i in cost:
            ma += i
            ct +=1
            if ma == coins:
                break
            elif ma>coins:
                ct -= 1
                break
        return ct
