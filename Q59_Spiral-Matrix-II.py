class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[None]*n for _ in range(n)]
        self.cnt = 1
        def dfs(y, x, last_way, directions=[(0, 1), (1, 0), (0, -1), (-1, 0)]):
            if y < 0 or y >= n or x < 0 or x >= n or mat[y][x] is not None:
                return 
            mat[y][x] = self.cnt
            self.cnt += 1
            dfs(y+last_way[0], x+last_way[1], last_way=last_way)
            for shift_y, shift_x in directions:
                dfs(y+shift_y, x+shift_x, last_way=(shift_y, shift_x))
        dfs(0, 0,(0, 1))
        return mat
            