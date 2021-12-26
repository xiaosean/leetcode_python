"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # Level order, we create a 2d list save each level of item
        def traverse(root, cnt=0, levels=[]):
            if not root:
                return levels
            if len(levels) <= cnt:
                levels += [[]]
            if levels[cnt]:
                root.next = levels[cnt][0]
            levels[cnt] = [root]
            traverse(root.right, cnt=cnt+1)
            traverse(root.left, cnt=cnt+1)    
            return levels
        levels = traverse(root)
        return root
        
            
        