class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        min_range = A[-1] - A[0]
        min_val = A[0]
        max_val_sub_k = A[-1] - K
        min_val = A[0] + K
        for idx in range(len(A)-1):
            cur_val = A[idx] + K
            next_val = A[idx+1] - K
            min_range = min(min_range, max(max_val_sub_k, cur_val) - min(min_val, next_val))
            # min_range = min(min_range, max_val_sub_k-min(cur_val, next_val))
        return min_range