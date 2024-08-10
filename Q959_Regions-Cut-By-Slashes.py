class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        h, w = len(grid), len(grid[0])
        #.     0
        #  3        1 
        #      2

        # create union graph
        parents = {}
        def find(x):
            if x not in parents or x == parents[x]:
                parents[x] = x
            else:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x, y):
            parents[find(x)] = find(y)

        
        for i in range(h):
            for j in range(w):
                if i:
                    union((i, j, 0), (i-1, j, 2))
                if j:
                    union((i, j, 3), (i, j-1, 1))
                if grid[i][j] != '/':
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))
                if grid[i][j] != '\\':
                    union((i, j, 0), (i, j, 3))
                    union((i, j, 1), (i, j, 2))
        return len(set([find(k) for k, _ in parents.items()]))