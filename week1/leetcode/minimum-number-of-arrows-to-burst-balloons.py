class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        x = 0
        arrow = 0
        for i in range(1,len(points)):
            ref = points[x][1]
            if points[i][0]>ref:
                arrow +=1
                x = i
            else:
                
                if ref > points[i][1]:
                    x = i
        arrow +=1
        return arrow



