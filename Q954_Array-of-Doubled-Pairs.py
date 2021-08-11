from collections import Counter
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter_arr = Counter(arr)
        arr.sort()
        n = len(arr)
        for item in arr:
            if not counter_arr[item]:
                continue
            counter_arr[item] -= 1
            if item >= 0:
                target_val = 2 * item
            else:
                target_val = 0.5 * item
            if counter_arr.get(target_val, 0) <= 0:
                return False
            counter_arr[target_val] -= 1
        return not any(counter_arr.values())