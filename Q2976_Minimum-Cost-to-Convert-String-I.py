class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # create table
        # adj = defaultdict(dict)
        n = 26
        adj = [[float('inf')]*n for _ in range(n)]
        for src, tgt, val in zip(original, changed, cost):
            adj[ord(src)-ord('a')][ord(tgt)-ord('a')] = min(adj[ord(src)-ord('a')][ord(tgt)-ord('a')], val)    
        for i in range(n):
            adj[i][i] = 0

        # @cache
        # def search_letter(src, dst):
        #     # bfs solution
        #     ans = float('inf')
        #     seen = set()
        #     heap = [(0, src)]
        #     while heap:
        #         val, x = heapq.heappop(heap)
        #         if x in seen:
        #             continue
        #         seen.add(x)
        #         for letter, cost in adj[x].items():
        #             if val + cost < ans and letter not in seen:
        #                 heapq.heappush(heap, (val+cost, letter))
        #                 if letter == dst:
        #                     ans = min(ans, val+cost)
        #     return ans if ans != float('inf') else None
        # Optimize graph
        for _ in range(2):
            for i in range(n):
                for j in range(n):
                    if adj[i][j] == float('inf'):
                        continue
                    for k in range(n):                        
                        if adj[j][k] == float('inf'):
                            continue
                        adj[i][k] = min(adj[i][k], adj[i][j] +  adj[j][k] )
            
        
        min_cost = 0
        for src, tgt in zip(source, target):
            if src != tgt:
                # val = search_letter(src, tgt)
                val = adj[ord(src)-ord('a')][ord(tgt)-ord('a')] if adj[ord(src)-ord('a')][ord(tgt)-ord('a')] != float('inf') else None
                if val is None:
                    return -1
                min_cost += val
        return min_cost