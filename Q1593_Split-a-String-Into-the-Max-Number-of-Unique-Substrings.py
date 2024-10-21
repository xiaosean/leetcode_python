class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        self.cnt = 0
        def backtracking(idx=0, path=None):
            if path is None:
                path = {}
            if idx == n:
                self.cnt = max(self.cnt, len(path))
                return
            for i in range(idx, n):
                if s[idx:i+1] not in path:
                    d = path.copy()
                    d[s[idx:i+1]] = True
                    backtracking(i+1, path=d)
        backtracking()
        return self.cnt
                