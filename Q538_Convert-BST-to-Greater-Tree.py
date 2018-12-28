# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        self.nodes = []
        def inorder_tree(root):
            if root:
                inorder_tree(root.left)
                self.nodes += [root]
                inorder_tree(root.right)
        inorder_tree(root)
        last_value = 0
        for node in self.nodes[::-1]:
            node.val += last_value
            last_value = node.val
            
        return root