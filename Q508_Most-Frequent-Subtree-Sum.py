# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def traverse(root):
            if not root:
                return None
            
            val = root.val
            for node in [root.left, root.right]:    
                if node:
                    val += traverse(node)
            frequency_table[val] = frequency_table.get(val, 0) + 1
            return val
        
        if not root:
            return None
#         init table
        frequency_table = {}
#       traverse node and add to table 
        traverse(root)
        max_val = max(frequency_table.values())
        res_list = []
        for key, val in frequency_table.items():
            if val == max_val:
                res_list += [key]
        return res_list
        