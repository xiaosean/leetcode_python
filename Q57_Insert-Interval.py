class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_s, new_e = newInterval
        l, r, merge = [], [], []
        for interval in intervals:
            start, end = interval
            if new_s > end:
                l += [interval]
            elif new_e < start:
                r += [interval]
            else:
                new_s = min(new_s, start)
                new_e = max(new_e, end)
        return l + [[new_s, new_e]] + r