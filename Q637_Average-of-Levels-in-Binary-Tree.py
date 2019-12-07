# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        def traverse_root(root, depth=0, collections=[]):
            if not root:
                return collections
            if depth >= len(collections):
                collections += [[]]
            collections[depth] += [root.val]
            for node in [root.left, root.right]:
                traverse_root(node, depth+1)
            return collections
        if not root:
            return None
        
        res = traverse_root(root)
        
        return [sum(level)/len(level) for level in res]