import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        flatten_list = [val for row in matrix for val in row ]
        heapq.heapify(flatten_list)
        return heapq.nsmallest(k, flatten_list)[-1]
        