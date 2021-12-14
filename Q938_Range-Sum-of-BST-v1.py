# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
        
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def traverse(root):
            if not root:
                return 0
            num = root.val if low <= root.val <= high else 0
            for node in [root.left, root.right]:
                if node:
                    num += traverse(node)
            return num
        return traverse(root)