class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        min_heap = [((x ** 2) + (y ** 2), i) for i, (x, y) in enumerate(points)]
        heapq.heapify(min_heap)
        
        res = []
        for _ in range(k):
            dist, i = heapq.heappop(min_heap)
            res.append(points[i])

        return res