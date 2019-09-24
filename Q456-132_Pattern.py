import bisect
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        seem_table = {}
        l_min_num = nums[0]
        r_nums = nums[1:]
        r_nums.sort()
        
        for idx in range(1, n-1):
            num = nums[idx]
            l_min_num = min(l_min_num, nums[idx-1])
            sorted_num_idx = bisect.bisect_left(r_nums, num)
            del r_nums[sorted_num_idx]
            if num <= l_min_num:
                continue
            
            if sorted_num_idx > 0 and r_nums[sorted_num_idx-1] > l_min_num:
                return True
        return False