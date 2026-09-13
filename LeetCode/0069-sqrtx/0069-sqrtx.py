class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        max_sqrt = 0
        while l <= r:
            m = (l + r) // 2
            if m*m > x: r = m - 1
            elif m*m < x:
                l = m + 1
                max_sqrt = max(max_sqrt, m)
            else: return m
        return max_sqrt