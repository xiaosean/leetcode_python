class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        cnt, fresh_orange = 0, 0
        cur_set, next_set = [], []
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 2:
                    cur_set += [(y, x)]
                elif grid[y][x] == 1:
                    fresh_orange += 1
        while cur_set:
            for (y, x) in cur_set:
                grid[y][x] = 2
                for shift_y, shift_x in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    next_y, next_x = y+shift_y, x+shift_x
                    if 0 <= next_y < len(grid) and 0 <= next_x < len(grid[0]) and grid[next_y][next_x]==1:
                        grid[next_y][next_x] = 2
                        next_set += [(next_y, next_x)]
                        fresh_orange -= 1
            if next_set:
                cnt += 1
            cur_set, next_set = next_set, []
        return cnt if fresh_orange == 0 else -1
            
        