class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        def find(x):
            if x not in parent:
                parent[x] = x
            elif parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)
        
        def check(x, y):
            if x in parent and y in parent:
                return find(x) == find(y)
            return False
        

        for x, y in edges:
            if check(x, y):
                return [x, y]
            union(x, y)
        
