class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        s = []
        for i,r in points:
            s.append(i)
        k = sorted(s)
        ma = 0
        for i in range(len(s)-1):
            c = (k[i+1]-k[i])
            ma = max(ma,c)
        return ma
        