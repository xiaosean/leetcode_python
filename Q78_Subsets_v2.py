class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ## dfs
        ## O(n^2)
        def dfs(nums, path=None, res=[[]]):
            if path:
                res += [path]
            if not nums:
                return res
            if path is None:
                path = []
            for idx, num in enumerate(nums):
                dfs(nums[idx+1:], path+[num])
            return res
        return dfs(nums)