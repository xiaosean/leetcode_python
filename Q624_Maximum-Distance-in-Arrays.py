class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_heap, max_heap = [], []
        for idx, arr in enumerate(arrays):
            x, y = arr[0], arr[-1]
            heapq.heappush(min_heap, (x, idx))
            heapq.heappush(max_heap, (-y, idx))
        res = 0
        for idx1 in range(len(arrays)):
            x, arr_idx1 = min_heap[idx1]
            for idx2 in range(len(arrays)):
                y, arr_idx2 = max_heap[idx2]
                if arr_idx1 == arr_idx2:
                    continue
                if -y-x <= res:
                    break
                res = -y-x
        return res
        