class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        size = len(grid)*len(grid[0])
        k = k % size
        l = []
        for row in grid:
            for x in row:
                l += [x]
        l = l[-k:] + l[:-k]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = l[i*len(grid[0])+j]
        return grid
                
        