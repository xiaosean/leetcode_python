class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        adj_mat = {}
        for from_, to_ in edges:
            adj_mat[from_] = adj_mat.get(from_, []) + [to_]
            adj_mat[to_] = adj_mat.get(to_, []) + [from_]
        visit = [False]*n
        def helper(from_, res=[]):
            if not visit[from_]:
                res += [from_]
                visit[from_] = True
                for to_ in adj_mat.get(from_, []):
                    helper(to_, res=res)
            return res
        cnt = 0

        for i in range(n):
            if visit[i]:
                continue
            arrive = helper(i, res=[])
            print(arrive)
            arr_cnt = len(arrive)
            cnt += arr_cnt*(n-arr_cnt)

        return cnt//2
            