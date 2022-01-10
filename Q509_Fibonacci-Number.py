class Solution:
    def fib(self, n: int) -> int:
        fib_0, fib_1 = 0, 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(2, n+1):
            fib_0, fib_1 = fib_1, fib_0+fib_1
        return fib_1
            