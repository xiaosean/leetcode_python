class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def dfs(start, target, path=None, res=[]):
            if path is None:
                path = []
            if start > len(candidates):
                return res
            
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num > target:
                    return res
                if num == target:
                    res += [path + [num]]
                    if len(res) > 1 and res[-1] == res[-2]:
                        res.pop()
                    return res
                dfs(i, target-num, path+[num], res)
            return res
        return dfs(0, target)
                        


