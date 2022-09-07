# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        s = ""
        if root:
            s += str(root.val)
            if root.left:
                s += f"({self.tree2str(root.left)})"
            if not root.left and root.right:
                s += "()"
            if root.right:
                    s += f"({self.tree2str(root.right)})"
            return s
        return ""