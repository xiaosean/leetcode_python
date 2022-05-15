# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.res = 0
        def traverse(root, depth=0):
            if not root:
                return 0
            if depth > self.max_depth:
                self.max_depth = depth
                self.res = 0
            if depth == self.max_depth:
                self.res += root.val
            for node in [root.left, root.right]:
                if node:
                    traverse(node, depth=depth+1)
        traverse(root)
        return self.res
                