class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # BFS-solution
        remaining = [set() for _ in range(n)] 
        adj = defaultdict(set)
        res = [set() for _ in range(n)]
        for from_, to in edges:
            adj[from_].add(to)
            remaining[to].add(from_)
        cur = deque()
        for i in range(n):
            if len(remaining[i])==0:
                cur.append(i)
        visit = set()
        while cur:
            node = cur.popleft()
            if node in visit:
                continue
            visit.add(node)
            for next_ in adj[node]:
                res[next_].add(node)
                for parent in res[node]:
                    res[next_].add(parent)
                remaining[next_].remove(node)
                if len(remaining[next_])==0:
                    cur += [next_]
        # filter the  duplicate ancestor
        res = [sorted(list(l)) for l in res]
        return res
            
