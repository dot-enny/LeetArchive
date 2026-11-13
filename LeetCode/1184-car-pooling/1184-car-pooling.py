class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key = lambda t : t[1])
        min_heap = []
        curr_pass = 0

        for t in trips:
            num_pass, start, end = t
            while min_heap and min_heap[0][0] <= start:
                curr_pass -= heapq.heappop(min_heap)[1]
            
            curr_pass += num_pass
            heapq.heappush(min_heap, (end, num_pass))
            if curr_pass > capacity: return False
        
        return True
            