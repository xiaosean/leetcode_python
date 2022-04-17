# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.vals = []
        def helper(root):
            while root:
                if root.right:
                    helper(root.right)
                self.vals = [root.val] + self.vals
                root = root.left
        helper(root)
        dummy = TreeNode()
        node = dummy
        for val in self.vals:
            node.right = TreeNode(val)
            node = node.right
        return dummy.right