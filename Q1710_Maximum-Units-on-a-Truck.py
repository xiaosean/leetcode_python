class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x:x[1], reverse = True)
        res = 0
        for count, unit in boxTypes:
            pick_count = min(truckSize, count)
            res += unit*pick_count
            truckSize -= pick_count
            if pick_count == 0:
                break
        return res
            
        