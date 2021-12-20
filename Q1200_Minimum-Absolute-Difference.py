class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        min_ = float('inf')
        for x, y in zip(arr[:-1], arr[1:]):
            diff = y-x
            if diff < min_:
                min_ = diff
                res = [[x, y]]
            elif diff == min_:
                res += [[x, y]]
        return res