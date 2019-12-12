from collections import deque
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = deque()
        if not grid:
            return None
        h, w = len(grid), len(grid[0])
        dist_grid = [[h+w]*w for _ in range(h)]
        for r_idx in range(h):
            for c_idx in range(w):
                val = grid[r_idx][c_idx]
                if val == 1:
                    dist_grid[r_idx][c_idx] = 0
                    q.append((r_idx, c_idx))
        largest_dist = -1
        while q:
            y, x = q.popleft()
            val = dist_grid[y][x]
            for next_y, next_x in [(y+1, x), (y-1, x), (y, x-1), (y, x+1)]:
                if 0 <= next_y < h and 0 <= next_x < w:
                    if 1+val < dist_grid[next_y][next_x]:
                        dist_grid[next_y][next_x] = 1 + val
                        q.append((next_y, next_x))
                        largest_dist = max(largest_dist, dist_grid[next_y][next_x])
                    
        return largest_dist