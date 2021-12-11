class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # we have 2 islands
        # First travering the island 2, pick up the islands to the list - dfs
        # check each sub-island2 is existed in island1 or not
        m, n = len(grid1), len(grid1[0])
        islands = []
        
        def traverse_island(y, x, path=None):
            if y < 0 or x < 0 or y >= m or x >= n or grid2[y][x] == 0:
                return 
            path += [(y, x)]
            grid2[y][x] = 0
            traverse_island(y-1, x, path)
            traverse_island(y, x-1, path)
            traverse_island(y+1, x, path)
            traverse_island(y, x+1, path)
            return path
        # Get all island in island2
        for y in range(m):
            for x in range(n):
                if grid2[y][x]:
                    islands += [traverse_island(y, x, path=[])]
        cnt = 0
        for subisland in islands:
            cnt += 1
            for y, x in subisland:
                if grid1[y][x] == 0:
                    cnt -= 1
                    break
        return cnt