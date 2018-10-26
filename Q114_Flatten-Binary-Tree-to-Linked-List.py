# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def traverse(root):
            r_list = [root]
            if root.left:
                r_list += traverse(root.left)
            if root.right:
                r_list += traverse(root.right)
            return r_list
        if root is None:
            return None
        nodes = traverse(root)
        root.left = root.right = None
        for idx, node in enumerate(nodes[1:]):
            node.left = None
            node.right = None
            nodes[idx].right = node
            