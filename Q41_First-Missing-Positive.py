class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        min_x = 2
        # max_x = 
        for i in range(n-1, -1, -1):
            if nums[i] < 1:
                del nums[i]
            else:
                min_x = min(min_x, nums[i])
        if min_x == 2:
            return 1
        n = len(nums)
        i = 0
        while i < n:
            num = nums[i]
            if num <= i:
#                 swap
                nums[num-1], nums[i] = num, nums[num-1]
                if nums[i] > num:
                    i -= 1
            i += 1

        pos = 0
        for i in range(n):
            pos += 1
            if pos != nums[i]:
                return pos
        return n+1