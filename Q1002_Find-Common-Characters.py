from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        counters = [Counter(a) for a in A]
        if counters:
            common_counter = counters[0]
            for counter in counters[1:]:
                common_counter = common_counter & counter
            s = []
            for k, v in common_counter.items():
                s += v * [k]
            return s
        return ""