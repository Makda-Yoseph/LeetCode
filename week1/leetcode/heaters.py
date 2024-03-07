class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def canheat(mid):
            l,r = 0,0
            while l<len(houses) and r<len(heaters):
                # print(2)
                if abs(houses[l]-heaters[r])>mid:
                    r+=1
                else:
                    l+=1
            if l>= len(houses):return True
            return False
        
        
        ans = 0
        left = 0
        right = max(houses[-1],heaters[-1])
        while left<=right:
            mid = (left+right)//2
           
            val = canheat(mid)
            if val :
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans
            
            
            
            