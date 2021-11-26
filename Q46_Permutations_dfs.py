class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path=None, res=[]):
            if path is None:
                path = []
            if not nums:
                res += [path]
            for idx, num in enumerate(nums):
                dfs(nums[:idx] + nums[idx+1:], path+[num], res=res)
            return res
        res = dfs(nums)
        return res