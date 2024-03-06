class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isitcapable(c):
            # q = deque(piles[:])
            # a=0
            # s=l=0
            d = 0
            # for i in range(d):
            # while len(q)!=0 and d<=h:
            #     if len(q)==0:
            #         return True
            #     if q:s+=q[l]
            #     if q:a=q.popleft()
           
            #     if s>c:
            #         q.appendleft(a-c)
            #     s= 0 
            #     d+=1
            for i in range(len(piles)):
                if piles[i]<= c:
                    d+=1
                else:
                    d+= ceil(piles[i]/c)

            if d<=h:
                return True
            else:
                return False
     
        ans = 0
        low= 1 
        high = max(piles)
        while low <= high:
            mid = (high + low)//2
            if isitcapable(mid)==True:
                ans = mid
                high = mid -1
            else:
                low = mid+1
        return ans