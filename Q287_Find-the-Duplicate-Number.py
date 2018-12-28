class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        n = len(nums)
        low = 1
        high = n - 1
        while True:
            if low == high:
                return low
            mid = int(low + (high -low)/2)
            # print("low = %d high = %d mid = %d"%(low, high, mid))
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
#           in low...mid
            if count <= mid:
                low = mid + 1
#           in mid+1...high
            else:
                high = mid
            