# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linked_list_helper import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = [head]
        cur = head
        length = 1
        while cur.next:
            stack.append(cur.next)
            cur = cur.next
            length += 1

        if length <= 2:
            return
        cur = head
        for i in range(length):
            if i%2 == 0:
                temp = cur.next
                cur.next = stack[-1]
                cur = temp
            else:
                stack[-1].next = cur
                stack.pop()

        if length % 2 == 0:
            cur.next = None
        else:
            stack[-1].next = None