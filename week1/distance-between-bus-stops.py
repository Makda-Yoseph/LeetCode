class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        
        if start < destination:
            p1 = sum(distance[start:destination])
            del distance[start:destination]
            p2=sum(distance)
            path = min(p1,p2)
        elif start > destination:
            p1 = sum(distance[destination:start])
            del distance[destination:start]
            p2 = sum(distance)
            path = min(p1,p2)
        return path

        