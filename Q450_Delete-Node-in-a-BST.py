# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent = dummy = TreeNode(None, left=root)
        # search the node
        node = root
        
        while node:
            if key == node.val:
                # handle parent
                if parent.left == node:
                    parent.left = node.right if node.right else node.left
                else:
                    parent.right = node.right if node.right else node.left
                if node.right is None:
                    break
                # handle children
                residual_left = node.left
                temp_node = node.right
                while temp_node and temp_node.left:
                    temp_node = temp_node.left
                temp_node.left = residual_left
                break
            parent = node
            if key > node.val:
                node = node.right
            else:
                node = node.left
        return dummy.left