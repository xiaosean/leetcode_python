class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # 2 pointer
        # while a or b finish -> bfs solution
        res = []
        a, b = None, None
        while firstList and secondList:
            if a is None:
                a = firstList[0]
            if b is None:
                b = secondList[0]
            if a[0] <= b[0] <= a[1] <= b[1]:
                res += [[b[0], a[1]]]
                a = None
                del firstList[0]
            elif b[0] <= a[0] <= b[1] <= a[1]:
                res += [[a[0], b[1]]]
                b = None
                del secondList[0]
            elif b[0] <= a[0] <= a[1] <= b[1]:
                res += [[a[0], a[1]]]
                a = None
                del firstList[0]
            elif a[0] <= b[0] <= b[1] <= a[1]:
                res += [[b[0], b[1]]]
                b = None
                del secondList[0]
            elif a[1] < b[0]:
                a = None
                del firstList[0]
            else:
                b = None
                del secondList[0]
        return res