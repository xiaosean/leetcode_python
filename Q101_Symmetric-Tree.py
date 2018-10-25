# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def traverse_tree(l_tree, r_tree):
            if l_tree.val != r_tree.val:
                return False
            if l_tree.left and r_tree.right:
                if traverse_tree(l_tree.left, r_tree.right) == False:
                    return False
            elif l_tree.left != None or r_tree.right != None:
                return False

            if l_tree.right and r_tree.left:    
                if traverse_tree(l_tree.right, r_tree.left) == False:
                    return False
            elif l_tree.right!= None or r_tree.left!= None:
                return False
            return True

        if root is None:
            return True
        if isinstance(root, TreeNode) and root.left==None and root.right==None:
            return True
        if isinstance(root, TreeNode) and root.left and root.right:
            return traverse_tree(root.left, root.right)
        else:
            return False
