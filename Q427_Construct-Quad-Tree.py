"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(i, j, s):
            if s == 0:
                return Node(val=grid[i][j], isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            tl = helper(i, j, s//2)
            tr = helper(i, j+s, s//2)
            bl = helper(i+s, j, s//2)
            br = helper(i+s, j+s, s//2)
            if tl.val==tr.val==bl.val==br.val and tl.isLeaf==tr.isLeaf==bl.isLeaf==br.isLeaf==True:
                return Node(val=tl.val, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            return Node(val=tl.val, isLeaf=False, topLeft=tl, topRight=tr, bottomLeft=bl, bottomRight=br)
        return helper(0, 0, len(grid)//2)