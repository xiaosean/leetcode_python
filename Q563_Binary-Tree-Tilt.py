# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        # using dfs and record the abs of each node
        self.res = []
        self.dfs(root)
        return sum(self.res)
        
    def dfs(self, node):
            l, r = 0, 0
            if not node:
                return 0
            if node.left:
                l = self.dfs(node.left)
            if node.right:
                r = self.dfs(node.right)
            abs_diff = abs(r - l)
            self.res += [abs_diff]
            return node.val + l + r
        