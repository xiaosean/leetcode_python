from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = Counter(deck)
        vals = [val for key, val in c.items()]
        min_val = min(vals)
        flags = [[val%i== 0 for val in vals] for i in range(2, min_val+1)]
        for f in flags:
            if all(f):
                return True
        return False