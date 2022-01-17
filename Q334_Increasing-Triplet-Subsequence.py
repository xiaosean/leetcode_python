class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        res = [nums[0]]
        for num in nums[1:]:
            if num > res[-1]:
                res += [num]
            else:
                idx = bisect_left(res, num)
                res[idx] = num
            if len(res) > 2:
                return True
        return False