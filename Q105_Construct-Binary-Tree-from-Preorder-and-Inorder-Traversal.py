# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) < 1:
            return None
    #     get root
        root = TreeNode(preorder[0])
    #     get inorder tree divide to two trees
        root_id = inorder.index(preorder[0])
        inorder_l_list = inorder[0:root_id]
        inorder_r_list = inorder[root_id+1:]
        
    #     get preorder tree
        preorder_l_list = preorder[1:len(inorder_l_list)+1]
        preorder_r_list = preorder[len(inorder_l_list)+1:]

        root.left = self.buildTree(preorder_l_list, inorder_l_list)
        root.right = self.buildTree(preorder_r_list, inorder_r_list)

        return root