class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = [[rStart, cStart]]
        nc, nr, d = 1, 0, 0
        while len(res) < rows*cols:
            for i in range(d//2+1):
                rStart += nr
                cStart += nc
                if rStart < 0 or rStart >= rows or cStart < 0 or cStart >= cols:
                    continue
                res += [[rStart, cStart]]
            nc, nr = nr, nc
            d += 1
            if d%2==0:
                nc, nr = -nc, -nr
            
        return res