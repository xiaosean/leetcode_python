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
        # Keep last level head and using dummy to current level
        # root -> hold last level
        # dummy -> hold current level
        
        current = dummy = Node(0) 
        head = root
        
        while root: 
            current = dummy
            while root:# traverse last level to connect the current level
                if root.left:
                    current.next = root.left
                    current = current.next
                if root.right:
                    current.next = root.right
                    current = current.next
                root = root.next # Key idea :traverse last level to next side!! 
            root = dummy.next # reset the root to current level for 
            dummy.next = None # clear the last level temp
        return head

