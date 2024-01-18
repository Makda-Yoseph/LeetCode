class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        mx = 0
        for m in range(len(trips)):
            mx = max(mx,trips[m][2])
        prefix = [0]*mx
        for t in trips:
            if t[0]>capacity:
                return False
            prefix[t[1]-1] += t[0]
            prefix[t[2]-1] +=(t[0]*-1)
        for j in range(1,len(prefix)):
            prefix[j] += prefix[j-1]
            if prefix[j]>capacity:
                return False
        return True
