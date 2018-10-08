class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        r = l = bisect.bisect_left(nums, target)

        if l >= len(nums) or nums[l] != target:
            return [-1, -1]

        for idx, num in enumerate(nums[l:]):
            if num == target:
                r = l + idx
            else:
                break
        return [l, r]