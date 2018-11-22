# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return None
        else:
            self.max_sum = root.val
        self.get_subtree_sum(root)
        return self.max_sum
    def get_subtree_sum(self, root):
        if root == None:
            return 0
        
        tree_sum_left = self.get_subtree_sum(root.left)
        tree_sum_right = self.get_subtree_sum(root.right)
        tree_sum = root.val + tree_sum_left + tree_sum_right
        self.max_sum = max(self.max_sum, root.val, tree_sum, root.val+tree_sum_left, root.val+tree_sum_right)
#         only pick one subtree right or left or this node
        return max(root.val, root.val+tree_sum_left, root.val+tree_sum_right)