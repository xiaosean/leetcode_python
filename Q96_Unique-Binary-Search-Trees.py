class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0 for _ in range(n+1)]
        G[0] = G[1] = 1

    #     2...n
        for i in range(2, n+1):
    #         0...i
            for j in range(1, i+1):
                G[i] += G[j-1]*G[i-j]
        return G[n]
