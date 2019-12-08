from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        q = deque()

    #     traverse each node, get zero node
        h, w = len(matrix), len(matrix[0])
        max_step = h * w
        for y in range(h):
            for x in range(w):
                node = matrix[y][x]
                if node == 0:
                    q.append((y, x))
                if node == 1:
                    matrix[y][x] = max_step

        while q:
            y, x = q.popleft()
            for next_step in[(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                next_y, next_x = next_step
                if 0 <= next_y < h and 0 <= next_x < w:
                    if 1 + matrix[y][x] < matrix[next_y][next_x]:
                        matrix[next_y][next_x] = 1 + matrix[y][x]
                        q.append(next_step)
        return matrix