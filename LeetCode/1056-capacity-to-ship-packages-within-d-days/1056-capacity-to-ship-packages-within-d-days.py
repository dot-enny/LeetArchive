class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        min_w = float('inf')
        while l <= r:
            m = (l + r) // 2
            acc, chunks = 0, 0
            for w in weights:
                if (acc + w) <= m: acc += w
                else: chunks, acc = chunks + 1, w
            chunks += 1
            if chunks <= days: 
                min_w = min(min_w, m)
                r = m - 1
            else: l = m + 1
                
        return min_w