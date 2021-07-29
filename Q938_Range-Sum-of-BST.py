# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
        
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if node:
                val = node.val
                if val >= low and val <= high:
                    self.res += val
                leaves = []
                if val > high:
                    leaves = [node.left]
                elif val < low:
                    leaves = [node.right]
                else:
                    leaves = [node.left, node.right]
                for leaf in leaves:
                    if leaf:
                        dfs(leaf)
        dfs(root)
        return self.res