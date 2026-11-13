class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = [] 
        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0: heapq.heappush(max_heap, (count, char, 0))
        
        prev, res = None, ""
        while max_heap or prev:
            if prev and not max_heap: return res

            cnt, char, used = heapq.heappop(max_heap)
            res += char
            cnt += 1
            used += 1
            if used < 2 and cnt != 0: heapq.heappush(max_heap, (cnt, char, used))

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if cnt != 0 and used > 1: prev = (cnt, char, 0)

        return res
