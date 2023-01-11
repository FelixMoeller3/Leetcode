# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from tree_helper import TreeNode

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return not subRoot
        if not subRoot:
            return True
        descendantIsSubtree = self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        if root.val != subRoot.val:
            return descendantIsSubtree
        return (self.treeEqual(root.left,subRoot.left) and self.treeEqual(root.right,subRoot.right)) or descendantIsSubtree

    def treeEqual(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return not root
        if not root:
            return False
        return root.val == subRoot.val and self.treeEqual(root.left,subRoot.left) and self.treeEqual(root.right,subRoot.right)