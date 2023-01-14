"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from typing import Optional


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # copy list
        if not head:
            return None
        oldNodeToIndex = {}
        newNodes = []
        cur = head
        newCur = None
        index = 0
        while cur:
            newNodes.append(Node(cur.val))
            if index > 0:
                newNodes[-2].next = newNodes[-1]
            oldNodeToIndex[cur] = index
            index += 1
            cur = cur.next
        cur = head
        randomPointerMap = {}
        index = 0
        while cur:
            if cur.random:
                randomPointerMap[index] = oldNodeToIndex[cur.random]
            else:
                randomPointerMap[index] = -1
            cur = cur.next
            index += 1
        for i in range(len(newNodes)):
            if randomPointerMap[i] == -1:
                newNodes[i].random = None
            else:
                newNodes[i].random = newNodes[randomPointerMap[i]]
        return newNodes[0]

