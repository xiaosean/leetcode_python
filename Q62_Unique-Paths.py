class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        L = m-1 + n-1
        mup_L = 1
        for i in range(1, L+1):
            mup_L *= i
        mup_m = 1
        for i in range(1, m):
            mup_m *= i
        mup_n = 1
        for i in range(1, n):
            mup_n *= i
        return int(mup_L / (mup_m*mup_n))