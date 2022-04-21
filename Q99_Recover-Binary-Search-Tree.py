# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # find not make sense nodes
        self.res = []
        def traverse(root):
            if root:
                traverse(root.left)
                self.res += [root]
                traverse(root.right)
        traverse(root)
        node1, node2 = None, None
        key_idx = 0
        for idx in range(len(self.res)-1):
            if self.res[idx].val > self.res[idx+1].val:
                key_idx = idx
                break
        node1 = self.res[key_idx]
        node2 = self.res[key_idx+1]
        for idx in range(key_idx+1, len(self.res)):
            if self.res[idx].val < node2.val:
                node2 = self.res[idx]
        node1.val, node2.val = node2.val, node1.val
            
                
        
                    