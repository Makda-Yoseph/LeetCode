class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        maxim = 0
        for i in range(len(points)-1):
            x = abs(points[i][0] - points[i+1][0])
            y = abs(points[i][1] - points[i+1][1])
            maxim += max(x,y)
        return maxim
        
        