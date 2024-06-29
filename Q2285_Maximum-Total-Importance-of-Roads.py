class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        connects = [0]*n
        for frm, to in roads:
            connects[frm] += 1
            connects[to] += 1
        res = 0
        for edge, weight in zip(sorted(connects), range(1, n+1)):
            res += edge*weight
        return res