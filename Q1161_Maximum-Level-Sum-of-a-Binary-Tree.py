# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        largest_level, largest_val = 1, root.val
        def traverse_tree(root, level=1, level_sets=[]):
            if root:
                if len(level_sets) < level:
                    level_sets.append([])
                level_sets[level-1] += [root.val]
                for node in [root.left, root.right]:
                    traverse_tree(node, level=level+1)
            return level_sets
        level_sets = traverse_tree(root)
        for level, level_set in enumerate(level_sets):
            sum_level = sum(level_set)
            if sum_level > largest_val:
                largest_val = sum_level
                largest_level = level+1
        return largest_level
        
        
        
     