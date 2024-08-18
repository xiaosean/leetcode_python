class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l = [1]
        cur, nex = [1], []
        visit = set([1])
        while cur:
            for num in cur:
                for i in [2, 3, 5]:
                    add_num = num*i
                    if add_num not in visit:
                        visit.add(add_num)
                        nex += [add_num]
            cur, nex = nex, []
            if len(visit) > 5*n:
                break
        return sorted(list(visit))[n-1]