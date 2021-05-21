# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:
    def _bfs(self, node):
        if node is None:
            return None
        for _node in [node.left, node.right]:
            if _node:
                self.node_list += [_node]
        if node.right is None and self.empty_index is None:
            self.empty_index = self.traverse_index
        
            
            
            
    def __init__(self, root: TreeNode):
        if root is None:
            return None
        self.traverse_index = 0
        self.empty_index = None
        self.node_list = [root]
        self.traverse_index = 0
        while self.traverse_index < len(self.node_list):
            self._bfs(self.node_list[self.traverse_index])
            self.traverse_index += 1
        if self.empty_index is None:
            self.empty_index = 0
        
        return None

    def insert(self, v: int) -> int:
        parent_node = self.node_list[self.empty_index]
        new_node = TreeNode(v)
        self.node_list += [new_node]
        if parent_node.left is None:
            parent_node.left = new_node
        else:
            parent_node.right = new_node
            self.empty_index += 1
        return parent_node.val

    def get_root(self) -> TreeNode:
        return self.node_list[0]


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()