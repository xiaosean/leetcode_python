class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        vals = {0:0}
        sum_ = 0
        for idx, val in enumerate(nums):
            sum_ += val
            if sum_ not in vals:
                vals[sum_] = idx+1
        min_cnt = len(nums)+1
        offset_val = 0
        for i in range(len(nums)):
            if i > 0:
                offset_val += nums[-i]
            if x-offset_val in vals:
                min_cnt = min(min_cnt, vals[x-offset_val]+i)
            
        return min_cnt if min_cnt < len(nums)+1 else -1