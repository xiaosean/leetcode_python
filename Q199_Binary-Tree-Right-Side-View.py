# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def traverse(root, depth=0, res=[]):
            if not root:
                return res
#             append node
            if len(res) <= depth:
                res += [0]    
            res[depth] = root.val
            for node in [root.left, root.right]:
                res = traverse(node, depth+1, res)
            return res
        return traverse(root)