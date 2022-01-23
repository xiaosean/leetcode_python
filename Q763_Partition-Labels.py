class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals_dict = {}
        for idx, letter in enumerate(s):
            if letter not in intervals_dict:
                intervals_dict[letter] = [idx, idx]
            else:
                intervals_dict[letter][1] = idx
        intervals = list(intervals_dict.values())
        print(intervals)
        intervals.sort()
        merged = []
        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged += [interval]
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        res = []
        print(merged)
        for start, end in merged:
            res += [end-start+1]
        return res