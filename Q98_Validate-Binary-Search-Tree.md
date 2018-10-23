# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root, small=None, large=None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if root.left is not None:
                if root.left.val >= root.val:
                    return False
                
                if large is not None and root.left.val >= large:
                    return False
                if small is not None and root.left.val <= small:
                    return False
#                 left set large
                if self.isValidBST(root.left, small=small, large=root.val) == False:
                    return False
            if root.right is not None:
                if root.right.val <= root.val:
                    return False
                if large is not None and root.right.val >= large:
                    return False
                if small is not None and root.right.val <= small:
                    return False
                if self.isValidBST(root.right, small=root.val, large=large) == False:
                    return False
        return True
        