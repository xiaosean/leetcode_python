# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.seen = {}
        stacks = []
        while root or stacks:
            if not root:
                while not root and stacks:
                    root = stacks.pop().right
                if not root:
                    break
            stacks.append(root)
            if k-root.val in self.seen:
                return True
            self.seen[root.val] = True
            root = root.left
        return False