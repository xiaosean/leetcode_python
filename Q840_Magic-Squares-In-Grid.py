class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def rule_check(x, y):
            sets = []
            diag1, diag2 = [], []
            nums = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if grid[i+x][j+y] > 9 or grid[i+x][j+y] < 1:
                        return False
                    nums += [grid[i+x][j+y]]
            if len(nums)!=len(set(nums)):
                return False
            for i in range(-1, 2):
                sets.append([grid[x+i][y], grid[x+i][y+1], grid[x+i][y-1]])
                sets.append([grid[x][y+i], grid[x+1][y+i], grid[x-1][y+i]])
                diag1 += [grid[x+i][y+i]]
                diag2 += [grid[x-i][y-i]]
            sets.append(diag1)
            sets.append(diag2)
            for s in sets:
                if sum(s) != 15:
                    return False
            return True
        cnt = 0
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if rule_check(i, j):
                    cnt += 1
        return cnt