# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Consider rob now or later
        def rob_or_not(node):
            dp = (0, 0)
            if not node:
                return dp
            left = rob_or_not(node.left)
            right = rob_or_not(node.right)
            # rob now
            now = node.val + left[1] + right[1]
            later = max(left) + max(right)
            return (now, later)
        return max(rob_or_not(root))