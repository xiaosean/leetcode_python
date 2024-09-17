class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        c1, c2 = Counter(s1.split()), Counter(s2.split())
        res = []
        for k in list(c1.keys()) + list(c2.keys()):
            if k in c1 and k in c2:
                continue
            for c in [c1, c2]:
                if k in c and c[k] == 1:
                    res += [k]
        return res