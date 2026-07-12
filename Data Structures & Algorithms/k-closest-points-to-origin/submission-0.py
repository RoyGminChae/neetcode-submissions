import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            distance = self.getDistance(x, y)
            heapq.heappush(heap, (distance, (x, y)))
    
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

    def getDistance(self, x, y):
        x = abs(x)
        y = abs(y)

        return math.sqrt(math.pow(x, 2) + math.pow(y, 2))