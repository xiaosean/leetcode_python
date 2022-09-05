"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        def dfs(root, level=0, res=[]):
            if root:
                if level == len(res):
                    res += [[]]
                res[level] += [root.val]
                for node in root.children:
                    dfs(node, level+1)
            return res
        return dfs(root)