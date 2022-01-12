class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        res = [[1], [1, 1]]
        idx = 2
        while idx <= rowIndex:
            res += [[1]]
            for i in range(1, idx):
                res[-1] += [res[-2][i-1] + res[-2][i]]
            res[-1] += [1]
            idx += 1
        return res[rowIndex]