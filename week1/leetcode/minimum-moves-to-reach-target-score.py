class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        for i in range((maxDoubles)):
            if target ==1:
                break
            rem = target %2
            target = target//2
            ans +=1
            if rem!=0:
                ans +=1
            
        ans += target -1
        return ans   