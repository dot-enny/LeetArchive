class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        min_capital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_capital)
        max_profit = []

        for i in range(k):

            while min_capital and min_capital[0][0] <= w:
                c, p = heapq.heappop(min_capital)
                heapq.heappush(max_profit, -p)

            if not max_profit: break

            w += -heapq.heappop(max_profit)

        return w

