# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        
        def dfs(node, path=None, sum_num=None, res=[]):
            if path is None:
                path = []
                sum_num = 0
            path += [node.val]
            sum_num += node.val
            if sum_num == targetSum and node.left is None and node.right is None:
                res += [path]
                return res
            for child_node in [node.left, node.right]:
                if child_node:
                    dfs(child_node, path=path.copy(), sum_num=sum_num)
            return res
        if root:
            return dfs(root)
        return None