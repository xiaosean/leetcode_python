# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def traverse(root, max_val=-float('inf')):
            if root:
                if root.val >= max_val:
                    max_val = max(max_val, root.val)
                return int(root.val >= max_val) + traverse(root.left, max_val) + traverse(root.right, max_val)
            return 0
        return traverse(root)