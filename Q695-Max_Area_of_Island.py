class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not isinstance(grid, list ) or not grid or not grid[0]:
            return 0
        h, w = len(grid), len(grid[0])
        def get_area(r_idx, c_idx, grid=grid):
            land = grid[r_idx][c_idx]
            if not land:
                return 0
            near_pos = []
#                 top
            if r_idx > 0:
                near_pos += [[r_idx-1, c_idx]]
#                 left
            if c_idx > 0:
                near_pos += [[r_idx, c_idx-1]]
#                 bottom
            if r_idx < h-1:
                near_pos += [[r_idx+1, c_idx]]
#                 right
            if c_idx < w-1:
                near_pos += [[r_idx, c_idx+1]]
            area = 1
#             set traverse
            grid[r_idx][c_idx] = 2
            for x, y in near_pos:
                if grid[x][y] == 1:
                    grid[x][y] = 2
                    area += get_area(x, y)
            return area
        
        max_area = 0
        for r_idx in range(h):
            for c_idx in range(w):
                max_area = max(max_area, get_area(r_idx, c_idx))
        return max_area
                