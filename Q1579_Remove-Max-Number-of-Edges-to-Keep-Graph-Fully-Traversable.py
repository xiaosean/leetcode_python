class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parent = {}
        
        def find(u):
            if u not in parent:
                parent[u] = u
            elif parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            parent[find(u)] = find(v)

        def check_full_connect(x, target):
            # print(f"x={x} find(x)={find(x)}, target = {target}")
            return find(x) == target

        
        res = 0
        ## create common edge
        for t, x, y in edges:
            if t == 3:
                if find(x) == find(y):
                    res += 1
                else:
                    union(x, y)
        
        for t, x, y in edges:
            if t == 1:
                if find(x) == find(y):
                    res += 1
                else:
                    union(x, y)

        for i in range(1, n+1):
            if i not in parent or not check_full_connect(i, find(1)):
                return -1
        
        parent = {}
        ## create common edge
        for t, x, y in edges:
            if t == 3:
                union(x, y)

        for t, x, y in edges:
            if t == 2:
                if find(x) == find(y):
                    res += 1
                else:
                    union(x, y)
        for i in range(1, n+1):
            if i not in parent or not check_full_connect(i, find(1)):
                return -1
            
        return res