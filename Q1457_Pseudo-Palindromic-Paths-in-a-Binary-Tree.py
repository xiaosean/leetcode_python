# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(root, num=0, res=[]):
            if not root:
                return res
            val = root.val
            num ^= 1<<val
            for node in [root.left, root.right]:
                if node:
                    dfs(node, num=num)
            if root.left is None and root.right is None:
                res += [num]
            return res 
        res = dfs(root)
        ans = 0
        for num in res:
            cnt = 0
            while num:
                if num % 2:
                    cnt += 1
                num >>= 1
            if cnt < 2:
                ans += 1
        return ans
               