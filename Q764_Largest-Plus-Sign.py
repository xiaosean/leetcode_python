class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        top_side = [0] * N
        left_side = [0] * N
        grids = [[1]*N for _ in range(N)]
        for x, y in mines:
            grids[x][y] = 0
        max_plus = 0
        for x in range(N):
            for y in range(N):
                if grids[x][y] == 1:
                    top_side[y] += 1
                    left_side[x] += 1
                else:
                    top_side[y] = 0
                    left_side[x] = 0
                    continue
                length = min(left_side[x], top_side[y])
                if length < max_plus:
                    continue
                right_side = 0
                for i in range(length):
                    if x+i < N and grids[x+i][y] == 1:
                        right_side += 1
                    else:
                        break
                bottom_side = 0
                for i in range(length):
                    if y+i < N and grids[x][y+i]:
                        bottom_side += 1
                    else:
                        break
                max_plus = max(max_plus, min(right_side, bottom_side))
        return max_plus