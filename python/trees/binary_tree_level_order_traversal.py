# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from tree_helper import TreeNode
from typing import List

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        allLevels = []
        curLevel = [root]
        while curLevel:
            nextLevel = []
            for node in curLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            allLevels.append([node.val for node in curLevel])
            curLevel = nextLevel
        return allLevels