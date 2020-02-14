# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def traverse(root, temp_sum, target, res=[]):
            if not root:
                return res
            temp_sum += root.val
            
            if temp_sum == target and root.left is None and root.right is None:
                res += [True]
                return res
            
            for node in [root.left, root.right]:
                if node:
                    traverse(node, temp_sum, target)
            return res
        return any(traverse(root, 0, sum))