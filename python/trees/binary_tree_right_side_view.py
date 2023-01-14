# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional,List
from tree_helper import TreeNode

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        rightSide = []
        curLevel = [root]
        while curLevel:
            nextLevel = []
            for node in curLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            rightSide.append(curLevel[-1].val)
            curLevel = nextLevel
        return rightSide