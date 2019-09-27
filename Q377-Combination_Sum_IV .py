class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        nums.sort()
        dp_ = [0] * (target+1)
        
        for subtarget in range(1, target+1):
            for num in nums:
                if subtarget - num == 0:
                    dp_[subtarget] += 1
#                 check memory
                elif subtarget - num > 0:
                    dp_[subtarget] += dp_[subtarget-num]
                else:
                    break
        return dp_[-1]
