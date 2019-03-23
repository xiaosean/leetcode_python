# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.leaves_val = []
        def traverse_root(root, prefix=0):
            if not root.left and not root.right:
                self.leaves_val += [prefix*10+root.val]
                return 
            [traverse_root(r, prefix*10+root.val) for r in [root.left, root.right] if r is not None]
        if root:
            traverse_root(root)
        return sum(self.leaves_val)
        