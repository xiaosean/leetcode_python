class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if mat is None:
            return None
        n, m = len(mat), len(mat[0])
        res = [[None] * m for _ in range(n)]
        
        queue = []
        for i in range(n):
            for j in range(m):
                val = mat[i][j]
                if val == 0:
                    res[i][j] = 0
                    queue += [(i, j)]
        while queue:
            i, j = queue[0]
            nearest_mat = []
            if i > 0:
                nearest_mat += [(i-1, j)]
            if i < n-1:
                nearest_mat += [(i+1, j)]
            if j > 0:
                nearest_mat += [(i, j-1)]
            if j < m-1:
                nearest_mat += [(i, j+1)]
            for near_i, near_j in nearest_mat:
                if res[near_i][near_j] is None:
                    res[near_i][near_j] = 1 + res[i][j]
                    queue += [(near_i, near_j)]
            queue = queue[1:]
        return res
