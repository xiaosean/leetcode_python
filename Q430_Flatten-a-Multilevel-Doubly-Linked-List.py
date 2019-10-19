"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        node = head
        flatten_head = Node(None, None, None, None)
        flatten_node = flatten_head
        node_stacks = []
        while node or node_stacks:
            if not node:
                node = node_stacks.pop()
#             link to next node
            flatten_node.next = Node(node.val)
#             let next node link to prev
            flatten_node.next.prev = flatten_node
#             shift to next node
            flatten_node = flatten_node.next
#           trace child first and put next to stack
            if node.child:
                if node.next:
                    node_stacks += [node.next]
                node = node.child
            else:
                node = node.next
        flatten_head.next.prev = None
        return flatten_head.next