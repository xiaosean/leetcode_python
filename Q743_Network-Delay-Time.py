from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
#         bfs solution
        bfs_queue = deque()
        dp_ = [None] * (N+1)
#       u v tables
        uv_pairs = {}
        for u, v, w in times:
            if u not in uv_pairs:
                uv_pairs[u] = []
            uv_pairs[u] += [(u, v, w)]
        
#         print(uv_pairs)
#         init bfs, setup the K node as start
        dp_[K] = 0
        for next_node in uv_pairs.get(K, []):
            bfs_queue.append(next_node)    
        while bfs_queue:
            u, v, w = bfs_queue.pop()
            if dp_[v] is None or dp_[u] + w < dp_[v]:
                dp_[v] = dp_[u] + w
                for next_node in uv_pairs.get(v, []):
                    bfs_queue.append(next_node)    
        del dp_[0]
        if None in dp_:
            return -1
        else:
            return max(dp_)
        
        