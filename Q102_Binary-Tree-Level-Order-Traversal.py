# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        l = [[]]
        level = 0
        stack = [(root, level)]
        while len(stack) > 0:
            r, level = stack[0]
            stack = stack[1:]
            if len(l) == level:
                l.append([])
            l[level] += [r.val]
            level += 1
            if r.left:
                stack += [(r.left, level)]
            if r.right:
                stack += [(r.right, level)]

        return l