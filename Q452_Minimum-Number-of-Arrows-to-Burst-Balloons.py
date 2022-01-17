class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        merged = []
        for point in points:
            if merged and (merged[-1][0] <= point[0] <= merged[-1][1]):
                merged[-1] = [max(merged[-1][0], point[0]), min(merged[-1][1], point[1])]
            else:
                merged.append(point)
        return len(merged)
                