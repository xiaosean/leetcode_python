# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def traverse_tree(root):
            r_list = []
            stack = []
            r = root
            while r or len(stack):
        #       traverse to left leaf
                if r is None:
                    r_list += ["null"]
                    
                while r:
                    stack += [r]
                    r = r.left
        #           no root means at leaf
                r_list += ["null"]
                r = stack.pop()
                r_list += [r.val]
                r = r.right
            return r_list

        p_list = traverse_tree(p)
        q_list = traverse_tree(q)
        if len(p_list) != len(q_list):
            return False
        else:
            for i in range(len(p_list)):
                if p_list[i] != q_list[i]:
                    return False
        return True


