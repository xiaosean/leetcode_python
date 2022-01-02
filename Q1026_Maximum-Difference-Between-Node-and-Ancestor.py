# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        self.max_diff_val = 0
        self.max_diff_val = 0
        def dfs(root, max_val=0, min_val=0):
            if not root:
                return 
            max_val = max(max_val, root.val)
            min_val = min(min_val, root.val)
            self.max_diff_val = max(self.max_diff_val, abs(max_val-root.val), abs(min_val-root.val))
            for node in [root.left, root.right]:
                if node:
                    dfs(node, max_val, min_val)
        dfs(root, root.val, root.val)
        return self.max_diff_val