# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # The most important thing of Linked list: pre_node and current
        null_node = ListNode(val=0, next=head)
        pre_node, node = null_node, head
        # 0 4 2 1 3
        while node:
            next_node = node.next # next_node = 2
            # insert node to insertion list
            pre_ins_node, ins_node = null_node, null_node.next # pre_ins_node = 0, ins_node = 4
            while ins_node and node != ins_node:
                # insert successful
                if node.val < ins_node.val:
                    pre_ins_node.next, node.next = node, pre_ins_node.next
                    pre_node.next = next_node
                    node = pre_node
                    break
                pre_ins_node, ins_node = ins_node, ins_node.next
            pre_node, node = node, next_node
        return null_node.next