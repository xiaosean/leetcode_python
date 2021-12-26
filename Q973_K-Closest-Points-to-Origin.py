import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (x*x+y*y, [x, y]))
        res = [point for dist, point in heapq.nsmallest(k, heap)]
        return res