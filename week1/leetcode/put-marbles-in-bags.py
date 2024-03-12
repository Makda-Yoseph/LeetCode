class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights)==2:
            return 0
        comb = []
        for i in range(0,len(weights)-1):
            print(weights[i])
            print(weights[i+1])
            comb.append((weights[i]+weights[i+1]))
        comb.sort()
        print(comb)
        j = k-1
        maxcost = 0
        i=0
        while j:
            maxcost+=comb[i]
            i+=1
            j-=1
        print(maxcost)
        j= k-1
        i = len(comb)-1
        mincost = 0
        while j:
            mincost+=comb[i]
            i-=1
            j-=1
        print(mincost)
        return (maxcost-mincost)*-1
            
