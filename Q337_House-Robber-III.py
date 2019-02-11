# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.node_dict = {}
        return self.traverse(root)
        
    def traverse(self, root, stop=False):
        if root is None:
            return 0
#         cache
        if stop and root in self.node_dict:
            return self.node_dict[root]
        
        # if stop traverse next:
        l = self.traverse(root.left)
        r = self.traverse(root.right)
        self.node_dict[root] = l+r
        if stop:
            return self.node_dict[root]
    
        current_traverse_money = 0
        if not stop:
            current_traverse_money = root.val + self.traverse(root.left, stop=True) +self.traverse(root.right, stop=True)
        return max(current_traverse_money, self.node_dict[root])
