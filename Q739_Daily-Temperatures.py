class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = {}
        warm_days = [0] * len(T)
        max_val = max(T)
        for idx, num in enumerate(T):
            for key, idxs in stack.items():
                if num > key:
                    for day_idx in idxs:
                        warm_days[day_idx] = idx-day_idx
                    stack[key] = []
            if num == max_val:
                warm_days[idx] = 0
            else:
                stack[num] = stack.get(num, []) + [idx]
        return warm_days