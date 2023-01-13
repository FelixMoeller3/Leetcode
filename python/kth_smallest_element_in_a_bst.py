# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from tree_helper import TreeNode

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodeList = []

        def inOrderTraversal(root: Optional[TreeNode]) -> None:
            if not root:
                return
            inOrderTraversal(root.left)
            nodeList.append(root.val)
            inOrderTraversal(root.right)

        inOrderTraversal(root)
        return nodeList[k-1]