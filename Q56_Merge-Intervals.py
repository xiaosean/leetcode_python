# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        interval_list = [(inrerval.start, inrerval.end) for inrerval in intervals]
        interval_list.sort()
        last_s, last_e = None, None
        r_list = []
        for s, e in interval_list:
            if last_s is None:
                last_s, last_e = s, e
                continue
                
    #         lasts s laste e
            if last_s <= s and s <= last_e and last_e <= e :
                last_e = e
    #         lasts s e laste 
            elif last_s <= s and s <= last_e:
                continue
    #        s lasts e laste but we sorted so it wouldn't happend
    #         elif last_s >= s and e >= last_s and last_e >= e:
    #         no match
            else:
                r_list += [Interval(last_s, last_e)]
                last_s = s
                last_e = e

        if last_s is not None:
            r_list += [Interval(last_s, last_e)]
        return r_list
