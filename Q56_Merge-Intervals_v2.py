class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        if len(intervals)==1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 1
        pre = intervals[0]
        res = []
        while i < len(intervals):
            curr = intervals[i]
            i += 1
            # intersect
            if max(pre[0], curr[0]) <= min(pre[1], curr[1]):
                interval = [min(pre[0], curr[0]), max(pre[1], curr[1])]
                pre = interval
            else:
                res += [pre]
                pre = curr
        res += [pre]
        return res
                
        