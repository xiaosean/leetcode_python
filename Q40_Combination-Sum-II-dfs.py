class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Solution 1
        # sorted
        # dfs 
        # for loop
        #   avoid get duplicate combination
        #   if current num == prev num:
        #       continue
        candidates.sort()
        
        def dfs(nums, path=None, sum_=0, res=[]):
            if path is None:
                path = []
            if  sum_ >= target:
                if sum_ == target:
                    res += [path]
                return res
            
            for idx, num in enumerate(nums):
                if idx == 0 or num != nums[idx-1]:
                    dfs(nums[idx+1:], path+[num], sum_+num, res)
            return res
        return dfs(candidates)