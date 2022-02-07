# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        self.stack = []
        
        def push_left(root):
            while root:
                self.stack += [root]
                root = root.left
        
        push_left(root)
        
        while self.stack:
            node = self.stack.pop()
            cnt += 1
            if cnt == k:
                return node.val
            push_left(node.right)
        return None
        