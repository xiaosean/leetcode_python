class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def helper(nums, k):
            if not nums:
                return 0
            pivot = random.choice(nums)
            left, mid, right = [], [], []
            for num in nums:
                if pivot > num:
                    left += [num]
                elif pivot < num:
                    right += [num]
                else:
                    mid += [num]
            if k <= len(left):
                return helper(left, k)
            if k > len(left)+len(mid):
                return helper(right, k-len(left)-len(mid))
            return mid[0]
        return helper(nums, len(nums)-k+1)