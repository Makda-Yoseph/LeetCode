class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isitcapable(c):
            q = deque(weights[:])
            a=0
            d = days
            while d>0:
                l = 0
                s = 0
                while s<c and  len(q)!=0:
                    s+=q[l]
                    if q:a=q.popleft()
                if s>c:
                    q.appendleft(a)
                d-=1
            if len(q)==0:
                return True
            else:
                return False
        ans = 0
        low= max(weights) 
        high = sum(weights)
        while low <= high:
            mid = (high + low)//2
            if isitcapable(mid)==True:
                ans = mid
                high = mid -1
            else:
                low = mid+1
        return ans
            
