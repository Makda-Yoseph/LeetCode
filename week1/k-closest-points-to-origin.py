class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
       sorted_points = sorted(points,key= lambda points:(points[0]**2 + points[1]**2)**0.5) 
       return sorted_points[:k]
        