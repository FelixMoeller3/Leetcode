# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linked_list_helper import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 1
        removableNode = None
        while cur.next:
            length += 1
            cur = cur.next
            if length == n+1:
                removableNode = head
            elif length > n+1:
                removableNode = removableNode.next
        if length == 1:
            return None
        if removableNode:
            removableNode.next = removableNode.next.next
        else:
            head = head.next
        return head

if __name__ == "__main__":
    head = ListNode(1)
    l = head
    for i in range(4):
        l.next = ListNode(i+2)
        l = l.next
    sol = Solution()
    sol.removeNthFromEnd(head,2)