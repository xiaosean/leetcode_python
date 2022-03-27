class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for j in range(len(mat[0])):
            for i in range(len(mat)):
                if mat[i][j] == 0 and i not in res:
                    res += [i]
                    if len(res) == k:
                        return res
        for i in range(len(mat)):
            if i not in res:
                res += [i]
                if len(res) == k:
                    return res
        
                    