class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        def dfs(y, x):
            if y < 0 or y > m-1 or x < 0 or x > n-1 or grid[y][x]!=1:
                return 0
            grid[y][x] =2
            ret = 1
            return ret + sum(dfs(y+shift_y, x+shift_x) for shift_y, shift_x in [[1, 0], [0, 1], [-1, 0], [0, -1]])
            
        def is_connected(y, x):
            return y==0 or (0<=y<m and 0<=x<n and any([grid[y+shift_y][x+shift_x]== 2 for shift_y, shift_x in [[1, 0], [0, 1], [-1, 0], [0, -1]] if 0<=y+shift_y<m and  0<=x+shift_x<n]))
        
        if not grid:
            return []
        m, n = len(grid), len(grid[0])
        
        for (y, x) in hits:
            grid[y][x] -= 1
                     
        for i in range(n):
            dfs(0, i)
            
        res = [0] * len(hits)
        for idx, (y, x) in enumerate(hits[::-1]):
            grid[y][x] += 1
            current_cnt = 0
            if grid[y][x] and is_connected(y, x):
                current_cnt = dfs(y, x)-1
            res[len(hits)-idx-1] = current_cnt
        return res