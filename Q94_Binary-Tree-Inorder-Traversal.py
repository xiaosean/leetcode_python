# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r_list = []
        if root is None:
            return r_list
        if root.left != None:
            r_list += self.inorderTraversal(root.left)
        r_list += [root.val]
        if root.right != None:
            r_list += self.inorderTraversal(root.right)
        return r_list