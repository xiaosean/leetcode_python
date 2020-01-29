class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        n = len(S)
        min_diff = sum([a != b for a, b in zip(S, n * "1")])
        dp_ = [min_diff] * (n+1)
        for zero_idx in range(n):
            if "0" == S[zero_idx]:
                dp_[zero_idx+1] = dp_[zero_idx] - 1
            else:
                dp_[zero_idx+1] = dp_[zero_idx] + 1
        
        return min(dp_)