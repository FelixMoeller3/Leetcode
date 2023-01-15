from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closestPoints = []
        distances = []
        distanceToPoints = {}
        for point in points:
            dist = (point[0]**2 + point[1]**2)
            distances.append(dist)
            if dist in distanceToPoints:
                distanceToPoints[dist].append(point)
            else:
                distanceToPoints[dist] = [point]
        heapq.heapify(distances)
        j = k
        while j>0:
            curDist = heapq.heappop(distances)
            for point in distanceToPoints[curDist]:
                closestPoints.append(point)
                j -= 1
        return closestPoints[:k]