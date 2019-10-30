# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def traverse(root, tgt_d, tgt_v, children=None, d=1):
            if not root:
                return
            
            if d+1 == tgt_d:
                children = [root.left, root.right]
                root.left = TreeNode(v)
                root.right = TreeNode(v)
                traverse(root.left, tgt_d, tgt_v, children=[children[0], None], d=d+1)
                traverse(root.right, tgt_d, tgt_v, children=[None, children[1]], d=d+1)
            else:
                if children:
#             link children
                    if children[0]:
                        root.left = children[0]
                    else:
                        root.right = children[1]
                    children = None
                traverse(root.left, tgt_d, tgt_v, children=children, d=d+1)
                traverse(root.right, tgt_d, tgt_v, children=children, d=d+1)


        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        else:
            traverse(root, d, v)
        return root