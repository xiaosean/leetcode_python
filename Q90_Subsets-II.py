class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def dfs(nums, path=None, res=[]):
            if path is None:
                path = []
            if not nums:
                if path not in res:
                    res += [path]
            last_num = None
            for i, num in enumerate(nums):
                dfs(nums[i+1:], path+[num], res)
                if last_num != num:
                    dfs(nums[i+1:], path, res)
                    last_num = num
            return res

        res = dfs(nums)
        if len(res) == 1:
            return []
        return res