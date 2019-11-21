class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall:
            return None
        w, h = sum(wall[0]), len(wall)
#         recording the gap index
        cross_map = {}
        for idx, row in enumerate(wall):
            gap_acc = 0
            for width in row:
                gap_acc += width
                cross_map[gap_acc] = cross_map.get(gap_acc, []) + [1]
        res = 0
        for k, v in cross_map.items():
            if k != w:
                res = max(res, sum(v))
        return h-res