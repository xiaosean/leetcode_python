from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Two pointer solution
        left and right,
        while l < r :
            next = max(node + left_step) for node in left
            l, r = r, next
        '''
        if len(nums) == 1:
            return 0
        if len(nums)-1 <= nums[0]:
            return 1
        l, r = 0, nums[0]
        cnt = 1
        while l < r:
            cnt += 1
            next_r = max([i + nums[i] for i in range(l, r+1)])
            if next_r >= len(nums)-1:
                return cnt
            l, r = r, next_r
        return cnt