class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dp_ = [[0] * 10 for _ in range(10)]
        for i, d in enumerate(dominoes):
            if d[0] > d[1]:
                dominoes[i][0], dominoes[i][1] = d[1], d[0]
        dominoes = sorted(dominoes, key=lambda x:(x[0], x[1]))
        cnt = 0
        for i in range(1, len(dominoes)):
            last, d = dominoes[i-1], dominoes[i]
            if d[0] == last[0] and d[1] == last[1]:
                dp_[d[0]][d[1]] += 1
                cnt += dp_[d[0]][d[1]]
        return cnt