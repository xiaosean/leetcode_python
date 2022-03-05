class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        cur = [poured]
        nex = None
        for i in range(query_row):
            nonzero = False
            nex = [0]*(i+2)
            for j in range(i+1):
                if cur[j] > 1:
                    nonzero = True
                    overflow = (cur[j]-1)/2
                    cur[j] = 1
                    nex[j] += overflow
                    nex[j+1] += overflow
            cur = nex
            if not nonzero:
                break
        if len(cur) < query_row+1:
            return 0
        return cur[query_glass] if cur[query_glass] < 1 else 1