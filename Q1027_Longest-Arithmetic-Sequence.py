class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if not A:
            return 0
        n = len(A)
        # A.sort()
        dp_ = {}
        
        for i in range(n-1):
            for j in range(i+1, n):
                dp_[j, A[j]-A[i]] = dp_.get((i, A[j]-A[i]), 1) + 1
        return max(dp_.values())
