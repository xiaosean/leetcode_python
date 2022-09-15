class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c = len(matrix), len(matrix[0])
        i, j = 0, 0
        visit = [[0] * c for _ in range(r)]
        cnt = 0
        res = []
        while cnt < r*c:
            cnt += 1
            visit[i][j] = 1
            res += [matrix[i][j]]
            for idx, (shift_y, shift_x) in enumerate(directions):
                next_y, next_x = i+shift_y, j+shift_x
                if 0 <= next_y < r and 0 <= next_x < c and visit[next_y][next_x] == 0:
                    i, j = next_y, next_x
                    directions = directions[idx:] + directions[:idx]
                    break
        return res