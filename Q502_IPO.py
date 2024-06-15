class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_profits = sorted(zip(capital, profits))
        l = 0
        heap_profits = []
        for _ in range(k):
            while l < len(profits) and capital_profits[l][0] <= w:
                capital, profit = capital_profits[l]
                heapq.heappush(heap_profits, -profit)
                l += 1
            if heap_profits:
                w -= heapq.heappop(heap_profits)
        return w