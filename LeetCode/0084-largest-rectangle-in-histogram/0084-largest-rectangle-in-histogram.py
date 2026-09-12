class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stores (index, height) tuples
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            if stack:
                if h >= stack[-1][1]:
                    stack.append((i, h))
                else:
                    start = 0
                    while stack and stack[-1][1] > h:
                        prev_area = (i - stack[-1][0]) * stack[-1][1]
                        max_area = max(max_area, prev_area)
                        start = stack.pop()[0]
                    stack.append((start, h))
            else: stack.append((i, h))
        
        n = len(heights)
        for h in stack[::-1]:
            area = (n - h[0]) * h[1]
            max_area = max(max_area, area)
        
        return max_area


