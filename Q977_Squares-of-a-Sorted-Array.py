class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        abs_nums = [abs(num) for num in nums]
        min_idx, min_val = 0, abs_nums[0]
        for idx, num in enumerate(abs_nums):
            if num < min_val:
                min_idx, min_val = idx, num
        l, r = min_idx-1, min_idx
        sortedSquares = []
        while l >= 0 and r < len(nums):
            l_val, r_val = nums[l]**2, nums[r]**2
            if r_val < l_val:
                sortedSquares += [r_val]
                r += 1
            else:
                sortedSquares += [l_val]
                l -= 1
        while l >= 0:
            l_val = nums[l]**2
            sortedSquares += [l_val]
            l -= 1
        while r < len(nums):
            r_val = nums[r]**2
            sortedSquares += [r_val]
            r += 1
        return sortedSquares