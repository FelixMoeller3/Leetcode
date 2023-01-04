# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linked_list_helper import ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2 or list2.val > list1.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        cur = head
        while list1 or list2:
            if not list1:
                cur.next = list2
                break
            if not list2:
                cur.next = list1
                break
            if list1.val < list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next

        return head