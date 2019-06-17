from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        groups = 0
        if n == 0 or n % W != 0:
            return False
        groups_num  = n // W
        c = Counter(hand)
        keys = list(c.keys())
        keys.sort()
        step = 0
        for _ in range(groups_num):
            groups = []
            step_lock = None
            for idx, k in enumerate(keys[step:step+W]):
                if c[k] > 0:
                    c[k] -= 1
                    if groups and k != groups[-1]+1:
                        return False
                    groups += [k]
                if step_lock is None and c[k] > 0:
                    step += idx
                    step_lock = True
            if step_lock is None:
                step += W
            if len(groups) < W:
                return False
        return True
        