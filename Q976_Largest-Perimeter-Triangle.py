from collections import Counter
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        n = len(A)
        A.sort(reverse=True)
        # print(A)
        for idx in range(n-2):
            largest_edge, next_edge_1, next_edge_2 = A[idx], A[idx+1], A[idx+2]
            if next_edge_1 < largest_edge / 2:
                continue
            if next_edge_1 + next_edge_2 > largest_edge:
                return next_edge_1 + next_edge_2 + largest_edge

        return 0