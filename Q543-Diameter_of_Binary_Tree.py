# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 1
        def traverse(root):
            if root is None:
                return 0
            l = traverse(root.left)
            r = traverse(root.right)
            self.count = max(self.count, l+r+1)
            return max(l, r)+1
        traverse(root)
        return self.count-1
