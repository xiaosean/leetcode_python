# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.count = 0
        self.sum_ = sum
        self.traverse(root)
        return self.count
    
    def traverse(self, root, nums_list=None):
        if root is None:
            return
        if root.val == self.sum_:
            self.count += 1
        if nums_list is None:
            nums_list = [root.val]
        else:
            for i in range(len(nums_list)):
                nums_list[i] += root.val
                if nums_list[i] == self.sum_:
                    self.count += 1
            nums_list += [root.val]
        self.traverse(root.left, nums_list.copy())
        self.traverse(root.right, nums_list.copy())
