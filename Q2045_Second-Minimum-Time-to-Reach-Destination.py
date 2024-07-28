class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        START = 1
        visit_cnt = [0]*(n+1)
        heap = [(0, START)]
        first_arrival_time = None
        mat = defaultdict(list)
        # handle the matrix
        for v1, v2 in edges:
            mat[v1].append(v2)
            mat[v2].append(v1)
        seen = [[] for _ in range(n+1)]
        while heap:
            val, v = heapq.heappop(heap)
            # If arrive the destination, Return the time elapse
            if v == n:
                if first_arrival_time is None:
                    first_arrival_time = val                 
                elif val > first_arrival_time:
                    return val
            if val//change % 2:
                    val = (val//change+1)*change
            for v2 in mat[v]:
                if not seen[v2] or len(seen[v2])==1 and seen[v2][0] != val:
                    seen[v2] += [val] 
                    heapq.heappush(heap,(val+time, v2))
        return -1