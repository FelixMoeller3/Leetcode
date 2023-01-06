# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from linked_list_helper import ListNode
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        nodes = {head}
        head = head.next
        while head:
            if head in nodes:
                return True
            nodes.add(head)
            head = head.next
        return False

    def hasCycleAlternate(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        firstPointer = head
        secondPointer = head.next
        while True:
            if not firstPointer:
                return False
            if not secondPointer or not secondPointer.next:
                return False
            if secondPointer == firstPointer or secondPointer.next == firstPointer:
                return True
            secondPointer = secondPointer.next.next
            firstPointer = firstPointer.next