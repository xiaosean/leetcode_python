# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        node = head
        while node:
            nodes += [node]
            node = node.next
        nodes[k-1].val, nodes[-k].val = nodes[-k].val, nodes[k-1].val
        return head