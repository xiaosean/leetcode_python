# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root):
            if root:
                val = root.val
                l = traverse(root.left)
                r = traverse(root.right)
                if l == 0:
                    root.left = None
                if r == 0:
                    root.right = None
                return val + l + r
            return 0
        dummy = TreeNode(val=0, left=root)
        traverse(dummy)
        return dummy.left