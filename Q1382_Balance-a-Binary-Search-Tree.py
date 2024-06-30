# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def traverse(root, res=[]):
            if root:
                traverse(root.left)
                res += [root.val]
                traverse(root.right)
            return res
        nums = traverse(root)
        def create_bst(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])
            mid = (l+r+1)//2
            root = TreeNode(nums[mid])
            root.left = create_bst(l, mid-1)
            root.right = create_bst(mid+1, r)
            return root
        return create_bst(0, len(nums)-1)
        
        

        
        