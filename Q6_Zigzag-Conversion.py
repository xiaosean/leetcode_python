class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        directions = [(1, 0), (-1, 1)]
        one_block = 2*numRows-2
        n_col = int(len(s)/one_block)
        if len(s)/one_block > len(s)//one_block:
            n_col += 1
        mat = [[""]*n_col*numRows for _ in range(numRows)]
        
        y, x, idx = 0, 0, 0
        direction = directions[0]
        while y < numRows and idx < len(s):
            mat[y][x] = s[idx]
            idx += 1
            if y == numRows-1:
                direction = directions[1]
            if y == 0:
                direction = directions[0]
            y, x = y+direction[0], x+direction[1]
        return "".join(["".join(row) for row in mat])