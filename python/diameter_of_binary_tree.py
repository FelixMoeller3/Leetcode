# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from tree_helper import TreeNode

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.right:
            if root.left:
                return max(self.depthOfBinaryTree(root.left),self.diameterOfBinaryTree(root.left))
            return 0
        if not root.left:
            return max(self.depthOfBinaryTree(root.right),self.diameterOfBinaryTree(root.right))
        return max(self.depthOfBinaryTree(root.left)+ self.depthOfBinaryTree(root.right),self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        

    def depthOfBinaryTree(self,root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.depthOfBinaryTree(root.left),self.depthOfBinaryTree(root.right))