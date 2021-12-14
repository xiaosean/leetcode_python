class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for i in range(len(nums))[::-1]:
            if nums[i] == val:
                cnt += 1
                nums[i], nums[-cnt] = nums[-cnt], nums[i]
        return len(nums)-cnt