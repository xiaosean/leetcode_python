class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def occlusion_(x=0, y=0):
            grid[y][x] = '0'
            if x+1 < n_cols and grid[y][x+1] == '1':
               occlusion_(x=x+1, y=y)
            if x-1 >= 0 and grid[y][x-1] == '1':
               occlusion_(x=x-1, y=y)
            if y+1 < n_rows and grid[y+1][x] == '1':
               occlusion_(x=x, y=y+1)
            if y-1 >= 0 and grid[y-1][x] == '1':
               occlusion_(x=x, y=y-1)
        n_rows = len(grid)
        if n_rows == 0:
            return 0
        n_cols = len(grid[0])
        
        island_count = 0
        for y in range(n_rows):
            for x in range(n_cols):
                if grid[y][x] == '1':
                    island_count += 1
                    occlusion_(x, y)
        return island_count
    