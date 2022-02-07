# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse_level(root, level=0, res=[]):
            if not root:
                return res
            if len(res) <= level:
                res.append([])
            res[level] += [root.val] 
            for node in [root.left, root.right]:
                traverse_level(node, level=level+1)
            return res
        res = traverse_level(root)
        for idx in range(len(res)):
            if idx%2 == 1:
                res[idx] = res[idx][::-1]
        return res