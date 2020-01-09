class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, tgt, path=None, res=[]):
            if path is None:
                path = []
            if path:
                sum_ = sum(path)
                if sum_ == tgt  and path not in res:
                    res += [path]
                elif sum_ > tgt:
                    return
            for idx, num in enumerate(nums):
                dfs(nums[idx+1:], tgt, path=path+[num])
            return res
        candidates.sort()
        return dfs(candidates, target)
                
            