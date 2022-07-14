# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, path=None, res=[]):
            if root is None:
                return None
            if path is None:
                path = []
            if root in [p, q]:
                res += [path]
            for node in (root.left, root.right):
                dfs(node, path+[node])
            return res
        res = dfs(root)
        same_node = root
        for i in range(min(len(res[0]), len(res[1]))):
            if res[0][i] == res[1][i]:
                same_node = res[1][i]
            else:
                break
        return same_node
        