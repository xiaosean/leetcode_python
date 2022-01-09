class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        n = len(points)
        largest = 0
        
        def gcd(a, b):
            if b==0: return a
            return gcd(b, a%b)
        
        for i in range(n):
            slope_dict = {}
            overlap = 0
            cur_max = 0
            for j in range(i+1, n):
                dx = points[j][0]-points[i][0]
                dy = points[j][1]-points[i][1]
                if dx==0 and dy==0:
                    overlap += 1
                    continue
                gcd_val = gcd(dx, dy)
                gcd_dx = dx//gcd_val
                gcd_dy = dy//gcd_val
                slope_dict[(gcd_dx, gcd_dy)] = slope_dict.get((gcd_dx, gcd_dy), 0) + 1
                cur_max = max(cur_max, slope_dict.get((gcd_dx, gcd_dy)))
            largest = max(largest, cur_max+overlap+1)
        return largest
        
        