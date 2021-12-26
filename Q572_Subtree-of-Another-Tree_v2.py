# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def compare_tree(root1, root2):
            if root1 is None and root2 is None:
                return True
            if (root1 and not root2) or (root2 and not root1):
                return False
            return root1.val==root2.val and compare_tree(root1.left, root2.left) and compare_tree(root1.right, root2.right)
        
        def traverse(root):
            if not root:
                return False
            return compare_tree(root, subRoot) or compare_tree(root.left, subRoot) or compare_tree(root.right, subRoot)
        
        def traverse_layer(root, target, cnt=0):
            if not root:
                return False
            if cnt <= target:
                return any([compare_tree(root, subRoot),
                        traverse_layer(root.left, target, cnt=cnt+1),
                        traverse_layer(root.right, target, cnt=cnt+1)])
            return any([traverse_layer(root.left, target, cnt=cnt+1),
                        traverse_layer(root.right, target, cnt=cnt+1)])
        
        
        def height_of_tree(root):
            if not root:
                return 0
            return 1+max(height_of_tree(root.left), height_of_tree(root.right))
        height_of_root = height_of_tree(root)
        height_of_subroot = height_of_tree(subRoot)
        target = height_of_root - height_of_subroot
        if target < 0:
            return False
            
        return traverse_layer(root, target)