# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse(root, res):
            if root:
                if root.left is None and root.right is None:
                    res += [str(root.val)]
                else:
                    for node in [root.left, root.right]:
                        if node:
                            traverse(node, res=res)
            return res
        return ",".join(traverse(root1, [])) == ",".join(traverse(root2, []))