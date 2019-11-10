# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def addNum(self, val: int) -> None:

        n = len(self.nums)
        if val >= n-1:
            self.nums += (val-n+2) * [False]
        self.nums[val] = True

    def getIntervals(self):
        intervals = []
        pre_num = -1
        n = len(self.nums)
        for idx in range(n):
            num = self.nums[idx]
            if num:
                if pre_num == -1:
                    pre_num = idx
            else:
                if pre_num != -1:
                    interval = [pre_num, idx-1]
                    # print(interval)
                    # print(interval.start, interval.end)
                    intervals.append(interval)
                    # print("end")
                pre_num = -1
        return intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()