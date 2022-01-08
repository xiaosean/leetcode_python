class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        def is_feasible(nums):
            hours = nums[0]*10 + nums[1]
            mins = nums[2]*10 + nums[3]
            return hours < 24 and mins < 60
        def permutation(nums, path=None, res=[]):
            if path is None:
                path = []
            if not nums:
                res += [path]
            for idx, num in enumerate(nums):
                permutation(nums[:idx]+nums[idx+1:], path+[num])
            return res
        res = []
        times = permutation(arr)
        times.sort(reverse=True)
        for time in times:
            if is_feasible(time):
                res = str(time[0]) + str(time[1]) + ":" + str(time[2]) + str(time[3])
                return res
        return ""
            
                
        