class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key=lambda x:x[1])
        # print(intervals)
        last_end = intervals[0][1]
        cnt = 0
        for interval in intervals[1:]:
            start, end = interval
            if start >= last_end:
                last_end = end
            else:
                cnt += 1
        return cnt
        