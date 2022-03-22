class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # 2 pointer solution
        res = ['a'] * n
        k -= n
        for i in range(n):
            if k >= 26:
                res[i] = 'z'
                k -= 25
            else:
                res[i] = chr(97+k%26)
                break
        return "".join(res)[::-1]
        