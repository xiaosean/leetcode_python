class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for idx1 in range(n-3):
            if idx1 > 0 and nums[idx1-1] == nums[idx1]:
                continue
            for idx2 in range(idx1+1, n-2):
                if idx2 > idx1+1  and nums[idx2-1] == nums[idx2]:
                    continue
                left = idx2+1
                right = len(nums)-1
                sub_target = target-nums[idx1]-nums[idx2]
                while left<right:
                    sum_ = nums[left] + nums[right]
                    if sum_ == sub_target:
                        res += [[nums[idx1], nums[idx2], nums[left], nums[right]]]
                        while left<right and nums[left+1] == nums[left]:
                            left += 1
                        while left<right and nums[right-1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif sum_ > sub_target:
                        right -= 1
                    else:
                        left += 1
        return res