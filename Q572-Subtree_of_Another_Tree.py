class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        self.t_root = t
        self.check_subtree = False
        def traverse(root):
            if root is None:
                return
            if root.val == self.t_root.val:
                if traverse_t_root(root, self.t_root):
                    self.check_subtree = True
                    return
            traverse(root.left)
            traverse(root.right)
            
        def traverse_t_root(root, t_root):
            if root is None and t_root is None:
                return True
            elif root is None or t_root is None:
                return False
            elif root.val == t_root.val:
                l = traverse_t_root(root.left, t_root.left)
                r = traverse_t_root(root.right, t_root.right)
                return l and r
            else:
                return False            
        if s is None and t is None:
            return True
        traverse(s)
        return self.check_subtree