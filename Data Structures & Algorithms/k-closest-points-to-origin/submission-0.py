import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(point):
            x = point[0]
            y = point[1]
            return math.sqrt(x*x + y*y) 
        
        distances = []
        for point in points:
            distances.append((distance(point),point))
        distances.sort()
        res = []
        print(distances)
        for i in range(k):
            res.append(distances[i][1])
        return res

