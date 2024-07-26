class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # bfs solution with hashmap to record the city has visited or not?
        adj = [[0] * n for _ in range(n)]
        for src, tgt, weight in edges:
            adj[src][tgt] = weight
            adj[tgt][src] = weight
        
        # bfs solution for each city
        def get_reachable_num(start, early_stop=n):
            reach_citys = [0]*n
            reach_citys[start] = n
            reachable_num = 0
            heap = [(-distanceThreshold, start)]
            while heap:
                threshold, cur = heapq.heappop(heap)   
                for i in range(n):
                    if adj[cur][i] and -threshold - adj[cur][i] >= reach_citys[i]:
                        if reach_citys[i] == 0:
                            reachable_num += 1
                            if reachable_num > early_stop:
                                return reachable_num
                        reach_citys[i] = max(-threshold - adj[cur][i], 1)
                        heapq.heappush(heap, (threshold+adj[cur][i], i))
                        
            return reachable_num
        
        min_num = n
        res = 0
        for i in range(n):
            reachable_num = get_reachable_num(i, min_num)
            if reachable_num <= min_num:
                min_num = reachable_num
                res = i
        return res
