class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ## dfs
        ## time complexity O(n^2)
        def dfs(nums, path=None, res=[]):
            if path:
                res += [path]
            if path is None:
                path = []
            for idx, num in enumerate(nums):
                if idx > 0 and num == nums[idx-1]:
                    continue
                dfs(nums[idx+1:], path=path+[num])
            return res
        nums.sort()
        return [[]] + dfs(nums)
                