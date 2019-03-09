class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return [nums]
        nums.sort()
        res = []
        
        def dfs(nums, res, path=None):
            if path is None:
                path = []
            n = len(nums)
            if n == 0:
                res += [path]
                return
            last = nums[0] - 1
            for i in range(n):
                if last == nums[i]:
                    continue
                dfs(nums[:i] + nums[i+1:], res,  path + [nums[i]])
                last = nums[i]
        dfs(nums, res, path=None)
        return res
    
    