class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        ## BFS solution
        v2v = defaultdict(dict)
        for idx, (v1, v2) in enumerate(edges):
            v2v[v1][v2] = succProb[idx]
            v2v[v2][v1] = succProb[idx]
        visit = set()
        cur = [[-1, start_node]]
        heapq.heapify(cur)
        max_prob = 0
        while cur:
            val, node = heapq.heappop(cur)
            if node in visit:
                continue
            visit.add(node)
            for k, v in v2v[node].items():
                cur_prob = -val*v
                if cur_prob < max_prob:
                    continue
                if k == end_node:
                    max_prob = max(max_prob, cur_prob)
                heapq.heappush(cur, [val*v, k])
        return max_prob