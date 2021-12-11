class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Using dfs to record all possible
        def dfs(nums, path=None, res=[]):
            if path is None:
                path = []
            if len(path) == k:
                res += [path]
                return res
            for idx, num in enumerate(nums):
                dfs(nums[idx+1:], path+[num], res)
            return res
        res = dfs(range(1, n+1))
        return res