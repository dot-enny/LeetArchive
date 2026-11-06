class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distances = [((p[0] ** 2) - 0) + ((p[1] ** 2) - 0) for p in points]
        max_heap = [(-d, i) for i, d in enumerate(distances)]
        heapq.heapify(max_heap)
        
        res = []
        while len(max_heap) > k:
            heapq.heappop(max_heap)

        for d, i in max_heap:
            res.append(points[i])

        return res