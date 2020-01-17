class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        n, m = len(A), len(A[0])
        trans_mat = [[0] * n for _ in range(m)]
        for r_idx in range(n):
            for c_idx in range(m):
                trans_mat[c_idx][r_idx] = A[r_idx][c_idx]
        return trans_mat