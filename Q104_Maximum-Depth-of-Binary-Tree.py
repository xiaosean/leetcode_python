# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root, count=1):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return count
        elif root.left and root.right is None:
            return self.maxDepth(root.left, count+1)
        elif root.right and root.left is None:
            return self.maxDepth(root.right, count+1)
        return max(self.maxDepth(root.left, count+1), self.maxDepth(root.right, count+1))
