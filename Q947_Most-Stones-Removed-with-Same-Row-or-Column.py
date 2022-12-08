class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Find how many cycles in the stones
        n = len(stones)
        cur, nex = stones, []
        cnt = 0
        set_y, set_x = set(), set()
        while cur:
            root_y, root_x = cur[0]
            set_y.add(root_y)
            set_x.add(root_x)
            can_remove = True
            while can_remove:
                can_remove = False                
                for y, x in cur[1:]:
                    if y in set_y or x in set_x:
                        set_y.add(y)
                        set_x.add(x)
                        cnt += 1
                        can_remove = True
                        continue
                    nex += [[y, x]]
                cur, nex = nex, []
                if can_remove:
                    cur = [[root_y, root_x ]] + cur
        return cnt