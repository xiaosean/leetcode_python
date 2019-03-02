class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        closet_num = sum(nums[:3])
        for i in range(1, n-1):
            pos = i
            start, end = 0, n-1
            while start < end:
                if start == pos:
                    start += 1
                    continue
                if end == pos:
                    end -= 1
                    continue
                sum_ = nums[pos] + nums[start] + nums[end]
                diff = sum_ - target
                if abs(closet_num - target) > abs(sum_ - target):
                    closet_num = sum_
                if diff > 0:
                    end -= 1
                elif diff < 0:
                    start += 1
                else:
                    return target
        return closet_num