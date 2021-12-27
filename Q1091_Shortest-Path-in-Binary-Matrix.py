from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # bfs solution
        # function visit - 8 directions
        # set 1 as infinitiy
        # start from (0, 0)
        if not grid:
            return False
        n, m = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1
        if grid[-1][-1] == 1:
            return -1
        
        
        for i in range(n):
            for j in range(m):
                grid[i][j] = float('inf') if grid[i][j] else grid[i][j]
        
        def eight_direct(y,x):
            if x < 0 or x >= m or y < 0 or y >=n:
                return
            res = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i==0 and j ==0:
                        continue
                    if x+j < 0 or x+j >= m or y+i < 0 or y+i >=n:
                        continue
                    res += [(y+i, x+j)]
            return res
        
        cnt = 1
        cur, nex = [(0, 0)], []
        while cur:
            for y, x in cur:
                if grid[y][x] == 0:
                    grid[y][x] = cnt
                    nex += eight_direct(y, x)
            cnt += 1
            cur, nex = nex, []
        
        return grid[-1][-1] if grid[-1][-1] != 0 else -1
        
        
        