class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrace(start, end, res = []):
            if start == end:
                res += [nums[:]] 
            for i in range(start, end):
                nums[start], nums[i] = nums[i], nums[start]
                backtrace(start+1, end)
                nums[start], nums[i] = nums[i], nums[start]
            return res
        return backtrace(0, len(nums))