class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # traverse each cell
        # if cell equals 1:
        #   count + 1 and using dfs flip the land of island to 0
        
        def flip_island(y, x):
            # if the grid is water, skip
            if grid[y][x] == '0':
                return 0
            # if the grid is land, then flip 1 to 0
            grid[y][x] = '0'
            # traverse 4 way
            traverse_way = []
            if x > 0:
                traverse_way += [(y, x-1)]
            if y > 0:
                traverse_way += [(y-1, x)]
            if x < n-1:
                traverse_way += [(y, x+1)]
            if y < m-1:
                traverse_way += [(y+1, x)]
            for next_y, next_x in traverse_way:
                flip_island(next_y, next_x)
        
        if not grid:
            return None
        m, n = len(grid), len(grid[0])
        cnt = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1':
                    cnt += 1
                    flip_island(y, x)
        return cnt
            