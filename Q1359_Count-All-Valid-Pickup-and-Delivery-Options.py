class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        for i in range(1, 2*n+1):
            res *= i
        return (res >> n) % (10**9+7)