# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def find_node(root, path=None, res=[]):
            if path is None:
                path = []
            if root:     
                if root == target:
                    res += [path]
                else:
                    find_node(root.left, path+["left"])
                    find_node(root.right, path+["right"])
            return res
        def executed_path(root, path):
            node = root
            for next_ in path:
                if next_ == "left":
                    node = node.left
                else:
                    node = node.right
            return node
        ans = find_node(original)
        clone_node = executed_path(cloned, ans[0])
        return clone_node
        