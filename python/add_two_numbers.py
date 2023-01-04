# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linked_list_helper import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # iterate over lists. In each pass add the current list nodes and 
        carry = 0
        val = l1.val + l2.val
        if val > 9:
            val -= 10
            carry = 1
        head = ListNode(val)
        l1 = l1.next
        l2 = l2.next
        prev = head
        while True:
            if not l1:
                leftOverList = l2
                break
            if not l2:
                leftOverList = l1
                break
            val = l1.val + l2.val + carry
            l1 = l1.next
            l2 = l2.next
            carry = 0
            if val > 9:
                val -= 10
                carry = 1
            cur = ListNode(val)
            prev.next = cur
            prev = cur
        
        while leftOverList:
            val = leftOverList.val + carry
            leftOverList = leftOverList.next
            carry = 0
            if val > 9:
                val -= 10
                carry = 1
            cur = ListNode(val)
            prev.next = cur
            prev = cur

        
        if carry == 1:
            prev.next = ListNode(1)
        return head