class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
#         calculate m => slope    
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        if x1-x0 == 0:
            return False
        m = (y1-y0)/(x1-x0)
        
        n = len(coordinates)
        for i in range(n-1):
            x0, y0 = coordinates[i]
            x1, y1 = coordinates[i+1]
            if x1-x0 == 0 or m != (y1-y0)/(x1-x0):
                return False
        return True