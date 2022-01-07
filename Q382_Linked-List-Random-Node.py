from random import randint
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.n = 0
        node = head
        while node:
            self.n += 1
            node = node.next
        
    def getRandom(self) -> int:
        node = self.head
        num = randint(0, self.n-1)
        n = 0
        while n < num:
            node = node.next
            n += 1
        return node.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()