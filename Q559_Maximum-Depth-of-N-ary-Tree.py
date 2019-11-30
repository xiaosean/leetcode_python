"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def traverse_depth(root, depth=0):
            if not root:
                return depth    
            depth += 1
            if not root.children:
                return depth
            return max(traverse_depth(node, depth) for node in root.children)
        return traverse_depth(root)