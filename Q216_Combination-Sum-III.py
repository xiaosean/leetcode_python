class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45:
            return []
        
        def dfs(nums, path=None, res=[]):
            if path is None:
                path = []
            
            if len(path) == k:
                if sum(path) == n:
                    res += [path]
                return res
            for idx, num in enumerate(nums):
                dfs(nums[idx+1:], path=path+[num])
            return res
        return dfs(list(range(1,10)))
    
            
                