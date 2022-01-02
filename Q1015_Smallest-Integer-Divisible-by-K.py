class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0 or k%5==0 :
            return -1
        num = 1
        cnt = 1
        while True:
            if not num % k:
                return cnt
            cnt += 1
            num = num *10 + 1
        