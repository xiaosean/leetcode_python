class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(l, k=1, path=None, res=[]):
            if not path:
                path = []
            if len(path) == k:
                res += [path]
                return
            for idx, item in enumerate(l):
                dfs(l[idx+1:], k=k, path=path+[item])
            return res
        return dfs(range(1, n+1), k)
